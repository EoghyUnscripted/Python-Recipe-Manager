class Instructions:

    def __init__(self):  # Initialize new step
        self.step = ''

    def getStep(self):  # Get step
        return self.step

    def setStep(self, step):  # Set step
        self.step = step

<<<<<<< HEAD
    def printSteps(self):  # Print step to console
=======
    def printSteps(self):  # Print recipe steps to console
>>>>>>> e726945... Initial Commit

        return (f'{self.getStep()}')

    def addStep(self):  # Add new step

<<<<<<< HEAD
        # Get step from user
        nextStep = input('Enter next step: \n')
        self.setStep(nextStep)  # Set step
=======
        nextStep = input('Enter next step: \n') # Get step from user
        self.setStep(nextStep)  # Set recipe instruction
>>>>>>> e726945... Initial Commit
