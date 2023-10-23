from Author import Author
from Diet import Diet
from Ingredient import Ingredient
from Instruction import Instruction

class Recipe:
    """Class object to store recipe data."""

    def __init__(self, name="Sandwich", author="Author", prep=0.0, cook=0.0, servings=0,
                 description = "Description", ingredients=[], instructions=[], dietary=[]):
        
        ### User-populated ###
        self.name = name
        self.author = author
        self.prep_time = prep   # In minutes
        self.cook_time = cook   # In minutes
        self.serving_size = servings
        self.description = description
        self.ingredient_list = ingredients
        self.instruction_list = instructions
        self.dietary_list = dietary    # List for dietary warnings
        
        ### Class-populated ###
        self._total_time = float(self.prep_time) + float(self.cook_time)
        self._ind_serving_cals = 0.0 # Individual serving calories
        self._total_recipe_cals = 0.0
        
### Functions ###

    def calculate_tot_time(self):
        """Function to calculate total recipe time."""
        
        self._total_time = float(self.prep_time) + float(self.cook_time)

    def calculate_tot_cals(self):
        """Function to calculate total recipe calories by looping through ingredients list."""
        
        for i in self.ingredient_list:
            
            self._total_recipe_cals += i._total_ingredient_cals
            
    def calculate_single_cals(self):
        """Function to calculate single serving calories."""
        
        self._ind_serving_cals = self._total_recipe_cals / float(self.serving_size)     # Divide total calories by serving count
    
### Methods ###

    def populate_author(self):
        """Method to create Author and set to recipe."""
        
        self.author = Author()
        self.author.promt()

    def populate_ingredients(self):
        """Method to prompt user for ingredients list."""
        
        recipe_ingredients = []
        
        while True:
            
            next_ingredient = Ingredient()
            next_ingredient.prompt()
            
            recipe_ingredients.append(next_ingredient)
            
            more_ingredients = input("Do you need more ingredients? (Y/N): ")

            if more_ingredients.lower() == "y":
                
                continue
            
            else:
                
                self.ingredient_list = recipe_ingredients                    
                break
            
    def populate_instructions(self):
        """Method to prompt user for instruction list."""
        
        recipe_instructions = []
        
        while True:
            
            next_instruction = Instruction()
            next_instruction.prompt()
            
            recipe_instructions.append(next_instruction)
            
            more_instructions = input("Are there more instructions to add? (Y/N): ")

            if more_instructions.lower() == "y":
                
                continue
            
            else:
                
                self.instruction_list = recipe_instructions                 
                break

    def populate_dietary(self):
        """Method to prompt user for dietary list."""
        
        recipe_dietary = []
        
        while True:
            
            next_dietary = Diet()
            next_dietary.prompt()
            
            recipe_dietary.append(next_dietary)
            
            more_dietary = input("Are there more dietary warnings to add? (Y/N): ")

            if more_dietary.lower() == "y":
                
                continue
            
            else:
                
                self.dietary_list = recipe_dietary                 
                break

    def print_summary(self):
        """Method to print formatted recipe summary to console."""

        print(
              f"\n{self.name}\n"
            + f"By: {self.author.full_name}\n"
            + f"\n"
            + f"Recipe Time: {self._total_time} minutes\n"
            + f"Total Calories: {self._total_recipe_cals}\n"
            + f"{self.description}\n"
        )
    
    def print_recipe(self):
        """Method to print formatted recipe to console."""
        
        # Print recipe details
        print(
              f"\n{self.name}\n"
            + f"By: {self.author.full_name}\n"
            + f"\n"
            + f"{self.description}\n"
            + f"\n"
            + f"Preparation Time: {self.prep_time} minutes\n"
            + f"Cook Time: {self.prep_time} minutes\n"
            + f"Yields: {self.serving_size} servings\n"
            + f"Single Serving Calories: {self._ind_serving_cals}\n"
            + f"Total Calories: {self._total_recipe_cals}\n"
        )
        
        # Print recipe ingredients if exists
        if len(self.ingredient_list) > 0:
            
            print("Ingredients\n")
            for i in self.ingredient_list:
                
                i.print_ingredient()
        
        # Print recipe instructions if exists
        if len(self.instruction_list) > 0:
            
            print("\nInstructions\n")
            for i in self.instruction_list:
                
                i.print_instruction()
            
        # Print recipe dietary warnings if exists
        if len(self.dietary_list) > 0:
            
            print("\nDietary\n")
            for i in self.dietary_list:
                
                i.print_dietary()
            print("\n")
        
### Main ###

    def prompt(self):
        """Prompts user to input recipe details."""
        
        while True:
            
            # Set Recipe details
            self.name = input("What should we call this recipe?: ")
            self.prep_time = input("How long does it take to prepare this recipe in minutes? (i.e. 2.5): ")   # In minutes
            self.cook_time = input("How long does it take to cook this recipe in minutes? (i.e. 12.5): ")   # In minutes
            self.serving_size = input("How many servings in this recipe?: ")
            self.description = input("Please add a short description of this recipe:\n")
            
            # Call methods to populate Author, Ingredients, Instructions, and Dietary
            self.populate_author()
            self.populate_ingredients()
            self.populate_instructions()
            self.populate_dietary()
            
            # Call functions to calculate total recipe calories, time, and individual serving calories
            self.calculate_tot_time()
            self.calculate_tot_cals()
            self.calculate_single_cals()
        
            # Verify recipe details with user
            print("Here is your new recipe: \n")
            print(50 * "*")
            self.print_recipe()
            print(50 * "*")
            looks_good = input(f"\nDoes this look good? (Y/N): ")

            if looks_good.lower() == "y":
                
                break
