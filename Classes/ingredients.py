class Ingredients:

    def __init__(self):  # Initialize new ingredient
        self.name = 'Blank'
        self.amount = 0.0
        self.measurement = 'cup, oz, etc'
        self.calories = 0.0
        self.comment = 'Comment'

    def getIngredientCalories(self):  # Get calories of ingredient
        return float(self.calories)

    def getIngredientName(self):  # Get name of ingredient
        return self.name

    def printIngredient(self):  # Print ingredient to console

        return (f'{self.amount} {self.measurement} '
                f'{self.name} '
                f'{self.comment}')

    def newIngredient(self):  # Add new ingredient to list

        while True:  # Loop until false

            try:
                self.name = input('What is the name of the ingredient?: '
                                  '\n')  # Get ingredient name

                self.amount = float(input('How much is needed (i.e. 2.5)?: '
                                          '\n'))  # Get ingredient amount

                self.measurement = input('What is the measurement (i.e. cup, '
                                         'oz)?: \n')  # Get measurement type

                # Get comment or special instruction
                self.comment = input('Comments (i.e. minced, chopped)?: \n')

                # Get ingredient calories
                self.calories = (float(input('How many calories are in '
                                             'this ingredient?: \n')))

            except Exception:

                # If input types are not integer
                print('Please input numbers for amount and calories, '
                      'Restarting...\n')

            finally:

                break  # Stop loop
