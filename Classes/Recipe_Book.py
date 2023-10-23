from Classes.Modules.Recipe import Recipe

class Book:
    "Class object to store cook book data."

    def __init__(self, name="Cook Book Name", recipes=[]):
        self.name = name
        self.recipe_list = recipes
        
    # TODO: Create a method to add a new recipe to the list
    def add_recipe(self):
        """Method to add recipe to the cook book."""
        
        print("Please enter recipe details:\n")
        
        rec = Recipe()
        rec.prompt()
        
        self.recipe_list.append(rec)
    
    # TODO: Create a method to view a recipe from the list
    def view_recipe(self, recipe):
        """Method to get recipe from the list and print to console."""
        
        self.recipe_list[int(recipe)].print_recipe()
    
    # TODO: Create a method to delete a recipe from the list
    def delete_recipe(self, recipe):
        """Method to delete recipe from book."""
        
        del self.recipe_list[int(recipe)]
    
    # TODO: Create a method to print recipe summaries
    
    # TODO: Create a menu for user 
    
    