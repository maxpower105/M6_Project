# Dice class notes:
# numbSides
# currentValue
# random number generator
#
# Functions
# Die(numSides)
# getCurrentValue: int
# roll: None
import random


class Die:
    def __init__(self, numSides):
        self.sides = numSides
        # do we need to set currentValue to something?
        self.__currentValue = self.roll()

    def getCurrentValue(self) -> int:
        return self.currentValue

    def roll(self) -> int:
        # has to roll the die
        # whats the math? need a random number, 1 through as many sides as their are
        # https: // docs.python.org / 3 / library / random.html
        # TODO add code to roll die
        self.currentValue = random.randint(1, int(self.sides))
        return self.currentValue # returning the value we just rolled makes sense here



""" # try it out code
sixSided = Die(6)
print(f"sides {sixSided.sides}")
print(f"current value {sixSided.getCurrentValue()}")
print(f"rolling: {sixSided.roll()}")
print(f"current value {sixSided.getCurrentValue()}")
 """

# look through the rest of the Battle Sim requirements (note vocab questions)
# think about the types tests you could write for this dice class
# (whats the input?, whats the expected output? how would a seed for the random generator
# help with tests?

