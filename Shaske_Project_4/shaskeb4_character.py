# MSOE CSC-5120-301
# Project 4
# Benjamin Shaske
# 6.20.2024

# Software Used
# Python V3.12.3
# PyCharm V2024.1.1 (Community)
# PyTest V8.2.2
# ----------------------------------------------------------------------------------------------------------------------

# Choose whether you will use duck typing (Protocol) or abstract base class for refactoring the mugwump and warrior
# classes. The goal is to have use two object references player (player controlled) and computer(computer controlled),
# which can each be either a warrior or a mugwump, and then allow the user to play out the game in the same ways as
# they did before. (20 pts)

""" Import necessary files."""
from shaskeb4_dice import Die


class Character:

    def __init__(self, aiController: bool):  # for homework 4 #, aiController:bool):
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.aiController = aiController
        self.hitPoints = 0


class Warrior(Character):
    """ Create a Warrior child class to the Character parent class."""

    def __init__(self, aiController):
        # call the constructor of the parent class
        super().__init__(aiController)

        # define unique Warrior attributes
        self.d8 = Die(8)
        self.d4 = Die(4)

        # hitpoints, max is set
        # Warrior uses four d10 to calculate their starting Hit Points.
        # we do this here, instead of in a separate method
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.hitPoints = self.maxHitPoints  # start perfectly healthy

    """
       This method asks the user what attack type they want to use and returns the result
       @return 1 for sword, 2 for shield
     """

    def attackChoice(
            self) -> int:  # this should be testable, see
        # https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call

        if self.aiController == True:
            print('AI Chooses the Warrior\'s attack!')
            attack_type = self.__ai()
            return attack_type
        else:
            choice = int(input("Choose the Warrior's attack.\n"  ### Need to cover the exception error handling on this.
                               "1. Your Trusty Sword\n"
                               "2. Your Shield of Light\n"
                               "Enter choice: "))
        return choice

    def attack(self, attack_type: int) -> int:
        # unlike mugwump, warrior's attack type is passed
        # in as a parameter.

        # roll attack die
        # determine results of attack
        damage = 0
        if attack_type == 1:  # trusty sword
            if self.d20.roll() >= 12:  # do we hit?
                damage = self.d8.roll() + self.d8.roll()  # 2d8 for damage
                print(f"You hit for {damage}")
            else:
                print("You miss!")
        else:  # (attack_type == 2): # shield of light
            if self.d20.roll() >= 6:  # do we hit
                damage = self.d4.roll()  # 1d4 damage
                print(f"You hit for {damage}")
            else:
                print("You miss")

        # return the damage
        return damage

    """
       This method determines what action the Mugwump performs
       @return 1 for a Claw attack, 2 for a Bite, and 3 if the Mugwump licks its wounds
     """

    def takeDamage(self, amount: int):
        if self.hitPoints >= amount:
            self.hitPoints -= amount
        else:
            self.hitPoints = 0

    def __ai(self) -> int:  # __ means private
        attack_type = 0
        roll = self.d20.roll()
        # 13 or greater on a d20
        if (roll <= 10):  # 50-50 odds
            # Your Trusty Sword
            attack_type = 1
            print('The Warrior attacks with his trusty sword!')
        else:
            # Your Shield of Light
            attack_type = 2
            print('The Warrior attacks with his shield of light!')

        return attack_type


# Mugwump Class---------------------------------------------------------------------------------------------------------
class Mugwump(Character):
    """ Create a Mugwump child class to the Character parent class."""

    def __init__(self, aiController):
        # call the constructor of the parent class
        super().__init__(aiController)

        # define unique Mugwump attributes
        self.d100 = Die(100)
        self.d6 = Die(6)

        # hitpoints, max is set
        # Mugwump uses six d10 to calculate their starting Hit Points.
        # we do this here, instead of in a separate method
        self.maxHitPoints = (self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() +
                             self.d10.roll())
        self.hitPoints = self.maxHitPoints  # start perfectly healthy

        # add methods here

    """
       This method handles the attack logic
       @return the amount of damage an attack has caused, 0 if the attack misses or
               a negative amount of damage if the Mugwump heals itself
     """

    def attackChoice(self) -> int:  # this should be testable, see
        # https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call

        if self.aiController == True:
            print('AI Chooses the Mugwump\'s attack!')
            attack_type = self.__ai()
            return attack_type
        else:
            choice = int(input("Choose the Mugwup's attack.\n"  ### Need to cover the exception error handling on this.
                               "1. Razor-Sharp Claws\n"
                               "2. Their Fangs of Death\n"
                               "3. Healing lick\n"
                               "Enter choice: "))
        return choice

    def attack(self, attack_type: int) -> int:

        # roll attack die
        # determine results of attack
        damage = 0
        if (attack_type == 1):
            if (self.d20.roll() >= 13):  # do we hit?
                damage = self.d6.roll() + self.d6.roll()  # 2d6
                print(f"Mugwump hits with claws for {damage}")
            else:
                print(f"Mugwump misses with claws")

        elif (attack_type == 2):
            if (self.d20.roll() >= 16):
                damage = self.d6.roll() + self.d6.roll() + self.d6.roll()  # 3d6
                print(f"Mugwump hits with fangs for {damage}")
            else:
                print(f"Mugwump misses with fangs")
        elif (attack_type == 3):  # else if was healing "lick wounds"
            damage = -1 * self.d6.roll()
            print(f"Mugwump heals for {-1 * damage}")

        # return the damage
        return damage  # range looks like -6 ... 0 .. 18. maybe test this 100 times

    """
       This method determines what action the Mugwump performs
       @return 1 for a Claw attack, 2 for a Bite, and 3 if the Mugwump licks its wounds
     """

    # this function allows for a negative amount, which is "healing"
    def takeDamage(self, amount: int):
        if (self.hitPoints >= amount):
            self.hitPoints -= amount
            # if we actually just healed, we should make sure
            # we don't exceed maxHitpoints
            if (self.hitPoints > self.maxHitPoints):
                self.hitPoints = self.maxHitPoints
        else:
            self.hitPoints = 0

    def __ai(self) -> int:  # __ means private
        attack_type = 0
        roll = self.d20.roll()
        # 13 or greater on a d20
        if (roll <= 12):  # 60%
            # Razor-Sharp Claws
            attack_type = 1
        elif (roll <= 17):  # 25%
            # Their Fangs of Death
            attack_type = 2
        else:
            # heal 15 %
            attack_type = 3

        return attack_type
