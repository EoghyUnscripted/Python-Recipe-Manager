from Classes import recipe


class box:

    recipeList = []  # Empty list for new recipes

    def __init__(self):
        self.recipeList = []

    def addNewRecipe(self):

        serving = 0  # Set method variable

        # Get name of new recipe
        recipeName = input('What is the name of your recipe?: \n')

        while True:

            try:
                # Get serving size
                serving = int(input('How many servings is the recipe?: \n'))
                break  # Stop loop

            except Exception:

                # If input is not an integer
                print('ERROR: \n',
                      'Please enter a valid serving as an integer.')

        newRecipe = recipe.Recipe(recipeName, serving)  # Create recipe object
        newRecipe.addIngredient()  # Call method to add ingredients to recipe
        newRecipe.addInstruction()  # Call method to add instructions to recipe

        self.recipeList.append(newRecipe)  # Append to recipe list in box

    def printRecipeList(self):  # Print recipeList items

        # Validates that the recipe list is not empty
        assert len(self.recipeList) != 0, "The Recipe Box is empty."

        i = 1  # Set for counter to print as string

        for row in range(len(self.recipeList)):  # Loop through recipe list

            print('{}.'.format(i), repr(self.recipeList[row].getRecipeName()),
                  '\n')  # Print number and recipe name
            i += 1  # Increment counter

        return self.recipeList[row].getRecipeName()  # Return the recipe

    print('\n')  # Print blank line

    def getRecipe(self, selection):  # Get user selected recipe

        # Validates that the recipe list is not empty
        assert len(self.recipeList) != 0, "The Recipe Box is empty."

        for row in range(len(self.recipeList)):  # Loop through recipe list

            # Matches recipe name selection to recipe list
            if (str(self.recipeList[row].getRecipeName()).lower()
                    == selection.lower()):

                # Print matched recipe from list
                return self.recipeList[row].printRecipe()

    def deleteRecipe(self, delete):  # Delete user selected recipe

        # Validates that the recipe list is not empty
        assert len(self.recipeList) != 0, "The Recipe Box is empty."

        tempList = self.recipeList

        for row in range(len(tempList)):  # Loop through recipe list

            # Matches recipe name selection to recipe list
            if (self.recipeList[row].getRecipeName().lower()
                    == delete.lower()):

                # Delete matched recipe from list
                self.recipeList.pop(row)
