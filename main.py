from Classes import recipeBox

<<<<<<< HEAD

=======
>>>>>>> e726945... Initial Commit
def menu():

    repeat = True  # Set boolean for loop
    selection = 0  # Set class variable

    while repeat is True:  # Return to menu after methods until exit

<<<<<<< HEAD
        # Print main menu
=======
        # Print user menu
>>>>>>> e726945... Initial Commit
        print(50 * '-' + '\n',
              10 * ' ' + 'Recipe Collection Manager' + 10 * ' ' + '\n' +
              50 * '-' + '\n',
              '\n',
              '1. Add Recipe \n',
              '2. Recipe List \n',
              '3. View Recipe \n',
              '4. Delete Recipe \n',
              '5. Quit \n',
              '\n' +
              50 * '-' + '\n')

        while True:
            try:
                selection = int(input('Choose a menu Option #: ')) # Get menu selection as integer
                print() # Print menu
                break

            except Exception:
                print('ERROR:\n',
                      'Please enter a numerical option. \n') # If input is not an integer

        if selection == 1:  # Add a new recipe

            myBox.addNewRecipe()  # Create new recipe object

        elif selection == 2:

            if myBox.printRecipeList() is False: # Checks if there are no recipes in list
                print('Please add a recipe, to use this option. \n') # Prompt user to add recipe first
                pass # Back to Menu

        elif selection == 3:

            if myBox.printRecipeList() is False: # Checks if there are no recipes in list
                print('Please add a recipe, to use this option. \n') # Prompt user to add recipe first
                pass # Back to Menu
            
            else:

                select = input('Please type the name of the recipe to view: \n') # Choose a recipe from the displayed list
                myBox.getRecipe(select)  # Print selected recipe from box

        elif selection == 4:

            if myBox.printRecipeList() is False: # Checks if there are no recipes in list
                print('Please add a recipe, to use this option. \n') # Prompt user to add recipe first
                pass # Back to Menu
            
            else:

                delete = input('Please select a recipe to delete: \n') # Choose a recipe from the displayed list
                myBox.deleteRecipe(delete)  # Delete selected recipe from box

        elif selection == 5:

            repeat = False  # Stop loop
            quit  # Exit program

myBox = recipeBox.box()  # Create new Recipe Box object
menu()  # Call main
