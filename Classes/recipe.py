from Classes import ingredients, instructions


class Recipe:

    def __init__(self, name, servings):  # Initialize new recipe
        self.name = name
        self.servings = servings
        self.ingredientList = []
        self.instructions = []
        self._totalCals = 0.0
        self._singleCals = 0.0

    def getRecipeName(self):  # Get recipe name
        return self.name

    def getRecipeServings(self):  # Get recipe servings
        return self.servings

    def getIngredientList(self):  # Get ingredients list

        # Loop through ingredients list
        for row in range(len(self.ingredientList)):

            print(self.ingredientList[row])  # Prints ingredients to console

    def getSingleCals(self):  # Get single calories
        return self._singleCals

    def getTotalCals(self):  # Get total calories
        return self._totalCals

    def setTotalCals(self, cals):  # Set total calories
        self._totalCals = cals

    def setSingleCals(self, single):  # Set single calories
        self._singleCals = single

    def calcTotalCalories(self):  # Calculate total recipe calories

        cals = 0.0  # Set counter

        # Iterate through ingredients list
        for row in range(len(self.ingredientList)):

            # Get ingredient calories and sums total
            cals += float(self.ingredientList[row].getIngredientCalories())

        self.setTotalCals(cals)  # Set total recipe calories

    def calcSingleCalories(self):  # Calculate single serving calories

        # Single serving calories is total recipe calories divided by servings
        single = (self.getTotalCals() / self.servings)

        self.setSingleCals(single)

    def printRecipe(self):  # Print recipe to console

        i = 1

        print(50 * '-' + '\n',
              20 * ' ' + self.getRecipeName(), '\n',
              50 * '-' + '\n',
              '\n',
              'Servings: ', self.getRecipeServings(), '\n',
              'Recipe Calories: ', self.getTotalCals(), '\n',
              'Serving Calories: ', self.getSingleCals(), '\n',
              '\n',
              'Ingredients: \n')

        # Iterate through ingredients list to print each row to console
        for row in range(len(self.ingredientList)):

            print(' ', self.ingredientList[row].printIngredient())

        print('\n',
              'Instructions: \n')

        # Iterate through instructions list to print each row to console
        for row in range(len(self.instructions)):

            print('  {}: '.format(i), self.instructions[row].printSteps())
            i += 1

        print('\n')

    def addIngredient(self):  # Add ingredients to recipe

        addMore = True  # Set boolean for loop

        while addMore is True:  # Repeat until false

            nextIng = ingredients.Ingredients()  # Create new ingredient object
            nextIng.newIngredient()  # Call function to set ingredient values

            # Append new ingredient to recipe ingredients list
            self.ingredientList.append(nextIng)

            # Ask user if they need to add another ingredient to loop
            add = input('Do you need another ingredient (Y/N)?: ')

            if add.lower() == 'y':
                addMore = True  # Loop again

            elif add.lower() == 'n':
                addMore = False  # Stop loop

                self.calcTotalCalories()  # Calculate Total Calories
                self.calcSingleCalories()  # Calculate Single Calories

            else:
                addMore = False  # Stop loop

                self.calcTotalCalories()  # Calculate Total Calories
                self.calcSingleCalories()  # Calculate Single Calories

    def addInstruction(self):  # Add ingredients to recipe

        addStep = True  # Set boolean for loop

        while addStep is True:  # Repeat until false

            # Create new instruction object
            nextStep = instructions.Instructions()
            nextStep.addStep()  # Call function to set instructions

            # Append new instructions to recipe instructions list
            self.instructions.append(nextStep)

            # Ask user if they need to add another step to loop
            add = input('Do you need to add another step (Y/N)?: ')

            if add.lower() == 'y':
                addStep = True  # Loop again

            elif add.lower() == 'n':
                addStep = False  # Stop loop

                break  # Break loop
