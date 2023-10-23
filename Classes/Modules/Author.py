class Author:
    """Class object to store Author data for each recipe."""
    
    def __init__(self, first="First", last="Last"):
        self.f_name = first
        self.l_name = last
        self.full_name = f"{self.f_name} {self.l_name}" # First Last
        
    def print_author(self):
        """Method used to print object as string to console."""
        
        print(self.full_name)
        
    def promt(self):
        """Prompts user to input first and last name for author object, updates full name."""
        
        while True:
            
            self.f_name = input("Author first name: ")
            self.l_name = input("Author last name: ")
            
            # Verify name with user
            looks_good = input(f"The author name is: {self.f_name.upper()} {self.l_name.upper()}\n"
                              +f"Is this correct? (Y/N): ")
            
            if looks_good.lower() == "y":
                
                # Update full name attribute
                self.full_name = f"{self.f_name} {self.l_name}"
                break
