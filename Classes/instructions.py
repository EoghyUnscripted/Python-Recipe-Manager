class Instructions:

    def __init__(self):  # Initialize new step
        self.step = ''

    def getStep(self):  # Get step
        return self.step

    def setStep(self, step):  # Set step
        self.step = step

    def printSteps(self):  # Print recipe steps to console

        return (f'{self.getStep()}')

    def addStep(self):  # Add new step

        nextStep = input('Enter next step: \n') # Get step from user
        self.setStep(nextStep)  # Set recipe instruction
