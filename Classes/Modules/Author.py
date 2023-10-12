class Author:
    """Class object to store Author data for each recipe."""
    
    def __init__(self, f_name="First", l_name="Last"):
        self.f_name = f_name    # First name
        self.l_name = l_name    # Last name
        self.full_name = f"{self.f_name} {self.l_name}" # Full name
        
    def get_f_name(self):
        """Class method to get first name."""
        
        return self.f_name  # Returns first name
    
    def set_f_name(self, name):
        """Class method to set first name."""
        
        self.f_name = name  # Sets first name
        
    def get_l_name(self):
        """Class method to get last name."""
        
        return self.l_name  # Returns last name
    
    def set_l_name(self, name):
        """Class method to set last name."""
        
        self.l_name = name  # Sets last name
        
    def get_full_name(self):
        """Class method to get full name."""
        
        return self.full_name   # Returns full name
    
    def set_full_name(self, first, last):
        """Class method to set full name."""
        
        self.full_name = f"{first} {last}"  # Sets full name