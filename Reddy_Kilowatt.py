from die_Ziller import Die
from Player_Ziller import Character
# I did warrior first so a lot was copied over

class Reddy_Kilowatt(Character):
    def __init__(self):
        super().__init__('Reddy_Kilowatt', [Die(12) for _ in range(4)])  # pull in name and hp
        self.d4 = Die(4)
        self.d6 = Die(6)

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
        if roll <= 16:
            return 1  # stab hertz
        elif roll <= 6:
            return 2  # lighting
        else:
            return 3  # recharge

    def attack(self, ai_controlled=False):
        if ai_controlled:
            attack_choice = self.__ai()
        else:
            print("How would you like to attack?")
            print("1. Stab Hertz")
            print("2. Lightning")
            print("3. Recharge")
            attack_choice = int(input("Enter choice: "))
        # added third choice for healing
        if attack_choice == 1:
            return self.stab_hertz(), "Stab Hertz"
        elif attack_choice == 2:
            return self.lighting(), "Lighining"
        elif attack_choice == 3:
            self.recharge()
            return 0, "Recharge"
        else:
            return 0, "Invalid Attack"

    def stab_hertz(self):
        hit_chance = self.d20.roll()
        if hit_chance >= 16: # 25% chance
            return sum(self.d4.roll() for _ in range(10))
        else:
            print("stab_hertz misses!")
            return 0

    def lighting(self):
        hit_chance = self.d20.roll()
        if hit_chance >= 6: # 75% chance
            return sum(self.d4.roll() for _ in range(1))
        else:
            print("Fangs of Death misses!")
            return 0

    def recharge(self):
        heal_amount = sum(self.d6.roll() for _ in range(3))
        self.hp = min(self.hp + heal_amount, self.max_hp)  # min function, used example from class to do this
        print(f"Reddy Kilowatt plugs in and recharges for {heal_amount} points!")

