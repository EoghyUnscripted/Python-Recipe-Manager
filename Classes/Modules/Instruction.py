class Instruction:
    """Class object to store instruction data for recipes."""

    def __init__(self, instruction="Stir the pot."):
        self.instruction = instruction

    def print_instruction(self):
        """Method used to print object as string to console."""
        
        print(self.instruction)
        
    def prompt(self):
        """Prompts user to input instruction details."""
        
        while True:
            
            print(f"Instruction Details")
            print() # Blank line
            
            self.instruction = input("\nWhat is the next step in the recipe?: ")
            
            # Verify instruction details with user
            looks_good = input(f"\nYou entered: {self.instruction}\nIs this correct? (Y/N): ")

            if looks_good.lower() == "y":
                
                break
