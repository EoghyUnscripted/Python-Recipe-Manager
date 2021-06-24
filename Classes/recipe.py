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

        for row in range(len(self.ingredientList)): # Loop through ingredients list

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

        for row in range(len(self.ingredientList)): # Iterate through ingredients list

            cals += float(self.ingredientList[row].getIngredientCalories()) # Get ingredient calories and sums total

        self.setTotalCals(cals)  # Set total recipe calories

    def calcSingleCalories(self):  # Calculate single serving calories

        
        single = (self.getTotalCals() / self.servings) # Single serving calories is total recipe calories divided by servings

        self.setSingleCals(single) # Set single serving calories count

    def printRecipe(self):  # Print recipe to console

        i = 1 # Set counter variable

        print(50 * '-' + '\n',
              20 * ' ' + self.getRecipeName(), '\n',
              50 * '-' + '\n',
              '\n',
              'Servings: ', self.getRecipeServings(), '\n',
              'Recipe Calories: ', self.getTotalCals(), '\n',
              'Serving Calories: ', self.getSingleCals(), '\n',
              '\n',
              'Ingredients: \n') # Print Recipe
        
        for row in range(len(self.ingredientList)): # Iterate through ingredients list to print each row to console

            print(' ', self.ingredientList[row].printIngredient()) # Print all ingredient rows in list

        print('\n',
              'Instructions: \n')  # Print Instructions

        for row in range(len(self.instructions)): # Iterate through instructions list to print each row to console

            print('  {}: '.format(i), self.instructions[row].printSteps()) # Print all instruction rows in list
            i += 1

        print('\n') # Blank Line

    def addIngredient(self):  # Add ingredients to recipe

        addMore = True  # Set boolean for loop

        while addMore is True:  # Repeat until false

            nextIng = ingredients.Ingredients()  # Create new ingredient object
            nextIng.newIngredient()  # Call function to set ingredient values

            self.ingredientList.append(nextIng) # Append new ingredient to recipe ingredients list

            add = input('Do you need another ingredient (Y/N)?: ') # Ask user if they need to add another ingredient to loop

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

            nextStep = instructions.Instructions() # Create new instruction object
            nextStep.addStep() # Call function to set instructions

            self.instructions.append(nextStep) # Append new instructions to recipe instructions list

            add = input('Do you need to add another step (Y/N)?: ') # Ask user if they need to add another step to loop

            if add.lower() == 'y':
                addStep = True  # Loop again

            elif add.lower() == 'n':
                addStep = False  # Stop loop

                break  # Break loop
