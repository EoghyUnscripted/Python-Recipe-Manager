class Ingredient:
    """Class object to store Ingredient data for recipes."""

    def __init__(self):
        self.name = "Blank" # Set ingredient name
        self.amount = 0.0   # Set ingredient amount
        self.measurement = "cup, oz, etc"   # Set ingredient measurement
        self.calories = 0.0     # Set ingredient calories
        self.comments = "Chopped, Diced, etc"   # Set ingredient comments

    def get_name(self):
        """Method to get ingredient name."""
        
        return self.name    # Return ingredient name
    
    def set_name(self, name):
        """Method to set ingredient name."""
        
        self.name = name    # Set ingredient name
        
    def get_amount(self):
        """Method to get ingredient amount for recipe."""
        
        return self.amount    # Return ingredient amount
    
    def set_amount(self, amount):
        """Method to set ingredient amount for recipe."""
        
        self.amount = amount    # Set ingredient amount
        
    def get_measurement(self):
        """Method to get ingredient measurement."""
        
        return self.measurement    # Return ingredient measurement
    
    def set_measurement(self, measurement):
        """Method to set ingredient measurement."""
        
        self.measurement = measurement    # Set ingredient measurement
        
    def get_calories(self):
        """Method to get ingredient calories."""
        
        return self.calories    # Return ingredient calories
    
    def set_calories(self, calories):
        """Method to set ingredient calories."""
        
        self.calories = calories    # Set ingredient calories
        
    def get_comments(self):
        """Method to get ingredient comments."""
        
        return self.comments    # Return ingredient comments
    
    def set_comments(self, comments):
        """Method to set ingredient comments."""
        
        self.comments = comments    # Set ingredient comments
