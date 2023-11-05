class Author:
    """Class object to create Author object ."""
    
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
            
            print(f"\nAuthor Details")
            print() # Blank line
            self.f_name = input("Enter author first name: ")
            self.l_name = input("Enter author last name: ")
            
            # Verify name with user
            looks_good = input(f"\nIs {self.f_name} {self.l_name} correct? (Y/N): ")
            
            if looks_good.lower() == "y":
                
                # Update full name attribute
                self.full_name = f"{self.f_name} {self.l_name}"
                break
