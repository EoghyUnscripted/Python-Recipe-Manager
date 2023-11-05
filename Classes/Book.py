from Modules.Recipe import Recipe
from Modules.Author import Author

class Book:
    "Creates a cook book object to collect and manage recipes."

    def __init__(self, name="Cook Book Name", author="Author", description="Delicious Recipes", recipes=[]):
        self.name = name
        self.author = author
        self.description = description
        self.recipe_list = recipes
        self.options = ["add","view","delete"]

    def add_recipe(self):
        """Method to add recipe to the cook book recipe list."""
        
        rec = Recipe()
        rec.prompt()
        
        self.recipe_list.append(rec)
    
    def view_recipe(self, recipe):
        """Method to get recipe from the list and print to console."""
        
        self.recipe_list[int(recipe)].print_recipe()
    
    def delete_recipe(self, recipe):
        """Method to delete recipe from cook book recipe list."""
        
        del self.recipe_list[int(recipe)]

    def populate_author(self):
        """Method to create Author and set to cook book."""
        
        self.author = Author()
        self.author.promt()
        
    def populate_recipes(self):
        """Method to create recipes and set to recipe list."""
        
        recipes = []
        
        while True:
            
            next_recipe = Recipe()
            next_recipe.prompt()
            
            recipes.append(next_recipe)
            
            more_recipes = input("Do you need to add more recipes? (Y/N): ")

            if more_recipes.lower() == "y":
                
                continue
            
            else:
                
                self.recipe_list = recipes                    
                break
    
    def print_all_recipes(self):
        """Method to print all recipe names from the cook book recipe list."""
        
        print(f"\nTable of Contents:\n")
        
        for i in range(0, len(self.recipe_list)):
            
            recipe = self.recipe_list[i]
            print(f"{(i + 1)}. {recipe.name}")
    
    def print_recipe_menu(self) -> int:
        """Method to print cook book recipe list to console. 
        Returns 0 if list is empty."""
        
        print(f"{self.name}\nBy: {self.author.full_name}\n\n{self.description}\n\n"
            + f"Table of Contents:\n")
        print("\n") # Blank line
           
        # Check for existing recipes
        if len(self.recipe_list) > 0:
            
            self.print_all_recipes()
        
        else:
            
            # If no recipes in book, return 0 for handling
            print(f"There are no recipes, yet.\n")
            return 0
 
    def print_options_menu(self):
        """Method to print cook book options menu to console."""
        
        # TODO: Create menu options for managing recipes in cook book
        pass
        
    def prompt(self):
        """Prompts user to enter cook book details and add recipes."""
        
        while True:
            
            # Set cook book details
            self.name = input("\nWhat should we call this cook book?: ")
            self.description = input("\nPlease add a short description of this cook book:\n")
            
            # Call methods to populate Author, Recipes
            self.populate_author()
            self.populate_recipes()
        
            # Verify cook book details with user
            print("\nHere is your cook book: \n")
            print(50 * "*")
            print("\n") # Blank line
            self.print_summary()
            print(50 * "*")
            
            looks_good = input(f"\nDoes this look good? (Y/N): ")

            if looks_good.lower() == "y":
                
                break
