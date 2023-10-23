class Ingredient:
    """Class object to store Ingredient data for recipes."""

    def __init__(self, amount=1, measurement="cup", name="Sugar", 
                 presentation="Granulated", calories=150.00):
        
        ### User-populated ###
        self.amount = amount
        self.measurement = measurement
        self.name = name
        self.presentation = presentation
        self.calories = calories
        
        ### Class-populated ###
        self._total_ingredient_cals = self.amount * self.calories
        
    def print_ingredient(self):
        """Method used to print object as string to console."""
        
        print(str(f"{self.amount} {self.measurement} {self.presentation} "
                + f"{self.name} -- {int(self.amount * self.calories)} calories").replace("  ", " ").replace(".0", ""))

    def prompt(self):
        """Prompts user to input ingredient details."""
        
        while True:
        
            print("Please enter the ingredient details.")
            
            self.amount = float(input("Amount or quantity: "))
            self.measurement = input("Measurement (i.e cups, oz, tsp): ")
            self.name = input("Ingredient name: ")
            self.presentation = input("Presentation (i.e. chopped, diced...)(optional): ")
            self.calories = int(input("Calories per measurement: "))
            
            # Verify ingredient details with user
            looks_good = input(str(f"{str(self.amount).replace('.0', '')} {self.measurement} {self.presentation} {self.name}\n"
                        + f"{int(self.amount * self.calories)} calories\nIs this correct? (Y/N): ").replace("  ", " "))

            if looks_good.lower() == "y":
                
                # Update total calories
                self._total_ingredient_cals = self.amount * self.calories
                break
