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

    def save_to_json(self, filename):
        character_info = {
            'name': self.name,
            'max_hitpoints': self.max_hp,
            'class': self.__class__.__name__
            # 'nickname': self.nickname
        }
        full_path = os.path.abspath(filename)
        with open(full_path, 'w') as f:
            json.dump(character_info, f, indent=4)
        print(f"Character saved to {full_path}")

    @classmethod
    def load_from_json(cls, filename):

        from mugwump_Ziller import Mugwump
        from Warrior_Ziller import Warrior
        from Reddy_Kilowatt import Reddy_Kilowatt

        full_path = os.path.abspath(filename)
        with open(full_path, 'r') as f:
            data = json.load(f)
        if data['class'] == 'Mugwump':
            character = Mugwump()
        elif data['class'] == 'Warrior':
            character = Warrior()
        elif data['class'] == "Reddy_Kilowatt":
            character = Reddy_Kilowatt()
        else:
            raise ValueError("Unknown character class in save file.")
        character.name = data['name']
        character.max_hp = data['max_hitpoints']
        character.hp = character.max_hp  # Assume the character is fully healed when loaded
        return character
