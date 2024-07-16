# MSOE CSC-5120-301
# Project 6
# Benjamin Shaske, Walter Ziller
# 6.20.2024

# Software Used
# Python V3.12.3
# PyCharm V2024.1.1 (Community)
# PyTest V8.2.2
# ----------------------------------------------------------------------------------------------------------------------

from die_Ziller_Shaske import Die
from Player_Ziller_Shaske import Character
# I did warrior first so a lot was copied over

class Reddy_Kilowatt(Character):
    def __init__(self):
        super().__init__('Reddy_Kilowatt', [Die(12) for _ in range(4)])  # pull in name and hp
        self.d4 = Die(4)
        self.d6 = Die(6)
        self.d10 = Die(10)
        self.charging_thunder = False # Add this for 4th attack

    def set_initial_hitpoints(self):  # setting initial hitpoints
        self.hp = sum(die.roll() for die in self.hp_dice)
        self.max_hp = self.hp

    def get_hitpoints(self):  # get current hitpoints
        return self.hp

    def take_damage(self, damage):  # general take damage math
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def __ai(self):  # make it hidden like in class example
        roll = self.d20.roll()
        if roll <= 14:
            return 1  # stab hertz
        elif roll <= 6:
            return 2  # lighting
        elif roll <= 2:
            return 4 # Thunder   # Add this for 4th attack
        else:
            return 3  # recharge

    def attack(self, ai_controlled=False):
        if ai_controlled:
            attack_choice = self.__ai()

            # Add this for 4th attack, this line is really importatn, this is how we go from charging ot attacking
        elif self.charging_thunder:  # this checks to see if charging is set to true, then thunder attack
            self.charging_thunder = False  # This resets the charging function back to false
            return self.thunder(), "Thunder!"  # Execute thunder attack if true
        else:
            print("\nHow would you like to attack?")
            print("1. Stab Hertz")
            print("2. Shock")
            print("3. Recharge")
            print('4. Thunder (two turn attack)')         # Add this for 4th attack
            select_flag = False
            while not select_flag:
                attack_choice = input("Enter choice: ")
                if (attack_choice.isdigit() and int(attack_choice) == 1)\
                        or (attack_choice.isdigit() and int(attack_choice) == 2)\
                        or (attack_choice.isdigit() and int(attack_choice) == 3)\
                        or (attack_choice.isdigit() and int(attack_choice) == 4):
                    select_flag = True
                else:
                    print('Not a valid input')
            print()

        # added third choice for healing
        if int(attack_choice) == 1:
            return self.stab_hertz(), "Stab Hertz"
        elif int(attack_choice) == 2:
            return self.shock(), "Lighining"
        elif int(attack_choice) == 3:
            self.recharge()
            return 0, "Recharging for healing power!"
        elif int(attack_choice) == 4:
            self.thunder_charge()       # Add this for 4th attack
            return 0, "nothing, Thunder Charging for next attack!" # need ot return 0 so damage attack result has a value
        else:
            return 0, "Invalid Attack"

    def stab_hertz(self):
        hit_chance = self.d20.roll()
        if hit_chance >= 16: # 25% chance
            return sum(self.d4.roll() for _ in range(10))
        else:
            print(f"\n{self.name}'s stab hertz attack misses!")
            return 0

    def shock(self):
        hit_chance = self.d20.roll()
        if hit_chance >= 6: # 75% chance
            return sum(self.d4.roll() for _ in range(1))
        else:
            print(f"\n{self.name}'s Shock attack misses!")
            return 0

    def recharge(self):
        heal_amount = sum(self.d6.roll() for _ in range(3))
        self.hp = min(self.hp + heal_amount, self.max_hp)  # min function, used example from class to do this
        print(f"{self.name} recharges for {heal_amount} points!")

    def thunder_charge(self):       #Add this for 4th attack
        self.charging_thunder = True
        print(f"{self.name} is charging Thunder!")

    def thunder(self):              # Add this for 4th attack
        charge = self.d20.roll() * 3
        hit_chance = self.d20.roll()
        if hit_chance >= 18: #18:  # 15% chance
            return sum(self.d10.roll() for _ in range(1)) + charge
        else:
            print(f"\n{self.name}'s charged Thunder attack misses")
            return 0

