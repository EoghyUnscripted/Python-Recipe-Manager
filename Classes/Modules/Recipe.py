from Classes.Modules import Ingredient, Author

class Recipe:
    """Class object to store recipe data."""

    def __init__(self):
        self.recipe_name = "Recipe Name"    # Recipe name
        self.author_name = "Author" # Author object
        self.prep_time = 0  # Recipe prep time
        self.cook_time = 0  # Recipe cook time
        self._total_time = 0 # Recipe total time
        self.serving_size = 0   # Serving size
        self.serving_cals = 0.0 # Individual serving calories
        self._total_cals = 0.0   # Total recipe calories
        self.ingredient_list = []   # List for ingredients
        self.prep_list = [] # List for preparation steps
        self.instruction_list = []  # List for cooking instructions
        self.dietary_list = []    # List for dietary warnings

    def get_recipe_name(self):
        """Class method to return recipe name."""
        
        return self.recipe_name # Return recipe name
    
    def set_recipe_name(self, name):
        """Class method to set recipe name."""
                
        self.recipe_name = name # Set recipe name

    def get_author_name(self):
        """Class method to return recipe author object to get name."""
        
        return self.author_name # Return author object

    def set_author_name(self, author):
        """Class method to update recipe author object with new author name."""
                
        self.author = author    # Set updated Author object as author name

    def get_prep_time(self):
        """Class method to return recipe prep time."""
        
        return self.prep_time   # Return prep time
    
    def set_prep_time(self, time):
        """Class method to set recipe prep time."""
        
        self.prep_time = time   # Return cook time
    
    def get_cook_time(self):
        """Class method to return recipe cook time."""
        
        return self.cook_time   # Return cook time
    
    def set_cook_time(self, time):
        """Class method to set recipe cook time."""
        
        self.cook_time = time   # Set cook time
 
    def get_total_time(self):
        """Class method to return total time to create recipe."""
        
        return self.total_time   # Return total cook time
    
    def set_total_time(self):
        """Class method to calculate and set total time to create recipe."""
                
        self.total_time = self.prep_time + self.cook_time   # Calculate and set total recipe time

    def get_serving_size(self):
        """Class method to return individual serving size."""
        
        return self.serving_size   # Return serving size
    
    def set_serving_size(self, size):
        """Class method to set individual serving size."""
        
        self.serving_size = size   # Set individual serving size
    
    def get_serving_cals(self):
        """Class method to return individual serving calories."""
        
        return self.serving_cals    # Return single serving calories
    
    def set_serving_cals(self):
        """Class method to set individual serving calories."""
        
        self.serving_cals = self.total_cals / self.serving_size # Set individual serving calories
    
    def get_total_cals(self):
        """Class method to return total recipe calories."""
        
        return self.total_cals  # Return total recipe calories
    
    def set_total_cals(self, calories):
        """Class method to set total recipe calories."""
        
        self.total_cals = calories  # Set new total calories
        
    def calc_total_cals(self):
        """Class method to calculate and set total recipe calories."""
        
        self.total_cals = self.serving_size * self.serving_cals  # Calculate and set total calories
    
    def get_ingredient_list(self):
        """Class method to return ingredients list."""
        
        return self.ingredient_list   # Return ingredients list
    
    def set_ingredient_list(self, ingredients):
        """Class method to set ingredients list."""
        
        self.ingredient_list = ingredients   # Set ingredients list
    
    def get_prep_list(self):
        """Class method to return preparation steps list."""
        
        return self.prep_list   # Return preparation steps list
    
    def set_prep_list(self, preparations):
        """Class method to set preparation steps list."""
        
        self.prep_list = preparations   # Set preparation steps list
    
    def get_instructions_list(self):
        """Class method to return instructions list."""
        
        return self.instruction_list   # Return instructions list
    
    def set_instructions_list(self, instructions):
        """Class method to set instructions list."""
        
        self.instruction_list = instructions   # Set instructions list
    
    def get_dietary_list(self):
        """Class method to return dietary warnings list."""
        
        return self.dietary_list   # Return dietary warnings list
    
    def set_dietary_list(self, dietary):
        """Class method to set dietary warnings list."""
        
        self.dietary_list = dietary   # Set dietary warnings list
