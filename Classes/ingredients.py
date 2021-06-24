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
        p_ingredient = str(self.amount) + ' ' \
            + str(self.measurement) + ' ' \
            + self.name + ' ' \
            + self.comment
        return p_ingredient

    def newIngredient(self):  # Add new ingredient to list

        while True:  # Loop until false

            try:
                self.name = input('What is the name of the ingredient?: '
                                  '\n')  # Get ingredient name

                self.amount = float(input('How much is needed (i.e. 2.5)?: '
                                          '\n'))  # Get ingredient amount

                self.measurement = input('What is the measurement (i.e. cup, '
                                         'oz)?: \n')  # Get measurement type

                self.comment = input('Comments (i.e. minced, chopped)?: \n') # Get comment or special instruction

                self.calories = (float(input('How many calories are in '
                                             'this ingredient?: \n'))) # Get ingredient calories

            except Exception:

                print('Please input numbers for amount and calories, '
                      'Restarting...\n') # If input types are not integer

            finally:

                break  # Stop loop
