from die_Ziller import Die
from Player_Ziller import Character

class Warrior(Character): # pass in super class
    def __init__(self):
        super().__init__('Warrior', [Die(10) for _ in range(4)])  # name and starting hp
        self.d8 = Die(8)
        self.d4 = Die(4)

    def set_initial_hitpoints(self):  # setting initial hitpoints
        self.hp = sum(die.roll() for die in self.hp_dice)
        self.max_hp = self.hp

    def get_hitpoints(self):  # get current hitpoints
        return self.hp

    def take_damage(self, damage):  # general take damage math
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_with_sword(self):
        hit_chance = self.d20.roll()
        if hit_chance >= 12:
            return sum(self.d8.roll() for _ in range(2))
        else:
            print("Trusty Sword misses")
            return 0

    def attack_with_shield(self):
        hit_chance = self.d20.roll()
        if hit_chance >= 6:
            return self.d4.roll()
        else:
            print("The Shield of Light misses!")
            return 0

    def __ai(self):  # make it hidden like in class example
        roll = self.d20.roll()
        if roll <= 12:  # 60% chance to use sword
            return 1  # Sword
        else:  # 40% chance to use shield
            return 2  # Shield

    def attack(self, ai_controlled=False):  # setting ai to false default
        if ai_controlled:
            attack_choice = self.__ai()
        else:
            print("How would you like to attack?")
            print("1. Your Trusty Sword")
            print("2. Your Shield of Light")
            attack_choice = int(input("Enter choice: "))

        if attack_choice == 1:
            return self.attack_with_sword(), "Trusty Sword"
        elif attack_choice == 2:
            return self.attack_with_shield(), "Shield of Light"
        else:
            return 0, "Invalid Attack"
