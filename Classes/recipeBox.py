from Classes import recipe

class box:

    recipeList = []  # Empty list for new recipes

    def __init__(self):
        self.recipeList = []

    def addNewRecipe(self): # Add new Recipe to Recipe Box

        serving = 0  # Set method variable
        
        recipeName = input('What is the name of your recipe?: \n') # Get name of new recipe

        while True:

            try:
                serving = int(input('How many servings is the recipe?: \n')) # Get serving size
                break  # Stop loop

            except Exception:
                
                print('ERROR: \n',
                      'Please enter a valid serving as an integer.') # If input is not an integer

        newRecipe = recipe.Recipe(recipeName, serving)  # Create recipe object
        newRecipe.addIngredient()  # Call method to add ingredients to recipe
        newRecipe.addInstruction()  # Call method to add instructions to recipe

        self.recipeList.append(newRecipe)  # Append to recipe list in box

    def printRecipeList(self):  # Print recipeList items

        # Validates that the recipe list is not empty in test
        # assert len(self.recipeList) != 0, "The Recipe Box is empty."

        if len(self.recipeList) < 1: # Checks recipe list count
            return False # If list is empty

        else:

            i = 1  # Set for counter to print as string

            for row in range(len(self.recipeList)): # Loop through recipe list

                print('{}.'.format(row), repr(self.recipeList[row].getRecipeName()),
                    '\n')  # Print number and recipe name
                i += 1  # Increment counter

            return self.recipeList[row].getRecipeName()  # Return the recipe

    def getRecipe(self, selection):  # Get user selected recipe

        # Validates that the recipe list is not empty in text
        #assert len(self.recipeList) != 0, "The Recipe Box is empty."

        if len(self.recipeList) < 1: # Checks recipe list count
            return False # If list is empty

        else:

            for row in range(len(self.recipeList)):  # Loop through recipe list
                
                if (str(self.recipeList[row].getRecipeName()).lower()
                        == selection.lower()): # Matches recipe name selection to recipe list
                    
                    return self.recipeList[row].printRecipe() # Print matched recipe from list

    def deleteRecipe(self, delete): # Delete user selected recipe

        # Validates that the recipe list is not empty in test
        # assert len(self.recipeList) != 0, "The Recipe Box is empty."

        if len(self.recipeList) < 1: # Checks recipe list count
            return False # If list is empty

        else:

            tempList = self.recipeList # Gets recipe list to modify

            for row in range(len(tempList)): # Loop through recipe list

                if (self.recipeList[row].getRecipeName().lower() # Matches recipe name selection to recipe list
                        == delete.lower()):
                    
                    self.recipeList.pop(row) # Delete matched recipe from list
