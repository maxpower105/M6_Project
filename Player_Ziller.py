# Creation of the super class to handle
# added the common items from the diagram shown in UML
# Functions had similar code in class examples, just modified slightly to be in super class
from abc import ABC, abstractmethod
from die_Ziller import Die
import json
from mugwump_Ziller import Mugwump
from Warrior_Ziller import Warrior

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

    def save_to_json(self, filename):
        character_info = {
            'name': self.name,
            'max_hitpoints': self.max_hp,
            'class': self.__class__.__name__
        }
        with open(filename, 'w') as f:
            json.dump(character_info, f, indent=4)

    def load_from_json(cls, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        if data['class'] == 'Mugwump':
            character = Mugwump()
        elif data['class'] == 'Warrior':
            character = Warrior()
        else:
            raise ValueError("Unknown character class in save file.")
        character.name = data['name']
        character.max_hp = data['max_hitpoints']
        character.hp = character.max_hp  # Assume the character is fully healed when loaded
        return character


















