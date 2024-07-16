# MSOE CSC-5120-301
# Project 6
# Benjamin Shaske, Walter Ziller
# 6.20.2024

# Software Used
# Python V3.12.3
# PyCharm V2024.1.1 (Community)
# PyTest V8.2.2
# ----------------------------------------------------------------------------------------------------------------------

import random

class Die:

    def __init__(self, numberSides:int): #testable
        # at least two sides and no more than 100, or set to 6
        if (numberSides < 2):
            numberSides = 6
        elif(numberSides > 100):
            numberSides = 6

        self.__numberSides = numberSides # __ means "private"
        #  set a seed that gives predicable
        # random.seed(1)
        self.currentValue = random.randint(1, self.__numberSides)  # set this randomly to start
        # for testing purposes, it may be helpful to try to use a seed, to set your
        # random number generator to return predictable

    # may not need
    # def getCurrentValue(self) -> int:
    #     return self.currentValue

    def roll(self) -> int: # testable
        # update self.numberSides
        self.currentValue = random.randint(1, self.__numberSides)
        return self.currentValue
