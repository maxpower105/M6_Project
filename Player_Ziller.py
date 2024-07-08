from die_Ziller import Die

# Creation of the super class to handle 
# added the common items from the diagram shown in UML
# Functions had similar code in class examples, just modified slightly to be in super class
from abc import ABC, abstractmethod
from die_Ziller import Die

# Creation of the super class to handle
# added the common items from the diagram shown in UML
# Functions had similar code in class examples, just modified slightly to be in super class
class Character(ABC):
    def __init__(self, name, hp_dice): # this class will determine the name and starting hp, starting hp will be finally determined in each character with a die roll
        self.d20 = Die(20)
        self.hp_dice = hp_dice
        self.hp = 0
        self.max_hp = 0
        self.name = name
        self.set_initial_hitpoints()

    @abstractmethod
    def set_initial_hitpoints(self): # setting intial hitpoints
        pass

    @abstractmethod
    def get_hitpoints(self):
        pass

    @abstractmethod
    def take_damage(self, damage): # general take damage maths
        pass

    @abstractmethod
    def attack(self):
        pass  # To be overridden in subclasses of warrior or mugwamp


















