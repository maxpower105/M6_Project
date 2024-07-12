import os
import json
from abc import ABC, abstractmethod
from die_Ziller import Die

class Character(ABC):
    def __init__(self, name=None, hp_dice=None):
        self.d20 = Die(20)
        self.hp_dice = hp_dice if hp_dice else []
        self.hp = 0
        self.max_hp = 0
        self.name = name
        if self.hp_dice:
            self.set_initial_hitpoints()
        # self.nickname = nickname

    @abstractmethod
    def set_initial_hitpoints(self):
        pass

    @abstractmethod
    def get_hitpoints(self):
        pass

    @abstractmethod
    def take_damage(self, damage):
        pass

    @abstractmethod
    def attack(self, ai_controlled=False):
        pass

    def save_to_json(self, filename): # similar to online examples
        character_info = {
            'name': self.name,
            'max_hitpoints': self.max_hp,
            'class': self.__class__.__name__
            # 'nickname': self.nickname
        }
        full_path = os.path.abspath(filename)
        with open(full_path, 'w') as f:
            json.dump(character_info, f, indent=4)
        print(f"Character saved to {full_path}") # added this for my mental health so i can see where its going on my pc

    @classmethod
    def load_from_json(cls, filename):
# had to import here b/c i kept getting a timing error
        from mugwump_Ziller import Mugwump
        from Warrior_Ziller import Warrior
        from Reddy_Kilowatt import Reddy_Kilowatt

        full_path = os.path.abspath(filename) # getting the file path
        with open(full_path, 'r') as f: # this opens th epath, similar to what we did in cars assignment
            data = json.load(f) # sets the loaded file to varialbe fo it can be itterated
        # looks at the class in the saved character and sets the class to the character
        if data['class'] == 'Mugwump':
            character = Mugwump()
        elif data['class'] == 'Warrior':
            character = Warrior()
        elif data['class'] == "Reddy_Kilowatt":
            character = Reddy_Kilowatt()
        else:
            raise ValueError("Unknown character class in save file.")

        # same thing here, looks at the name and max hp, no need to use if here as its just a value
        character.name = data['name']
        character.max_hp = data['max_hitpoints']
        character.hp = character.max_hp  # fully heals loaded character
        return character
