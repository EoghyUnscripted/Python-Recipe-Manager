from Classes import recipeBox


def menu():

    repeat = True  # Set boolean for loop
    selection = 0  # Set class variable

    while repeat is True:  # Return to menu after methods until exit

        # Print main menu
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
                # Get menu selection as integer
                selection = int(input('Choose a menu #: '))
                print()
                break

            except Exception:
                # If input is not an integer
                print('ERROR:\n',
                      'Please enter a numerical option. \n')

        if selection == 1:  # Add a new recipe

            myBox.addNewRecipe()  # Create new recipe object

        elif selection == 2:

            myBox.printRecipeList()  # Print Recipes in box

        elif selection == 3:

            myBox.printRecipeList()  # Print Recipes in box

            # Choose a recipe from the displayed list
            select = input('Please type the name of the recipe to view: \n')

            myBox.getRecipe(select)  # Print selected recipe from box

        elif selection == 4:

            myBox.printRecipeList()  # Print Recipes in box

            # Choose a recipe from the displayed list
            delete = input('Please select a recipe to delete: \n')

            myBox.deleteRecipe(delete)  # Delete selected recipe from box

        elif selection == 5:

            repeat = False  # Stop loop
            quit  # Exit program


myBox = recipeBox.box()  # Create new Recipe Box object
menu()  # Call main
