class Diet:
    """Class object to store dietary data for recipes."""

    def __init__(self, diet="Gluten-free"):
        self.diet = diet
        
    def print_dietary(self):
        """Method used to print object as string to console."""
        
        print(self.diet)

    def prompt(self):
        """Prompts user to input dietary details."""
        
        while True:
            
            self.diet = input("What dietary warning would you like to add? (i.e. Gluten-free): ")
            
            # Verify Dietary details with user
            looks_good = input(f"You entered: {self.diet}\nIs this correct? (Y/N): ")

            if looks_good.lower() == "y":
                
                break
