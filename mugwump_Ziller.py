from die_Ziller import Die
from Player_Ziller import Character

# I did warrior first so a lot was copied over
class Mugwump(Character):
    def __init__(self):
        super().__init__('Mugwump', [Die(10) for _ in range(6)]) # pull in name and hp
        self.d6 = Die(6)

    def __ai(self): # make it hidden like in class example
        roll = self.d20.roll()
        if roll <= 12:
            return 1  # Razor-Sharp Claws
        elif roll <= 17:
            return 2  # Fangs of Death
        else:
            return 3  # Heal
    # refer to warrior notes, copied over structure
    def attack(self, ai_controlled=False):
        if ai_controlled:
            attack_choice = self.__ai()
        else:
            print("How would you like to attack?")
            print("1. Razor-Sharp Claws")
            print("2. Fangs of Death")
            print("3. Lick Wounds")
            attack_choice = int(input("Enter choice: "))
        # added third choice for healing
        if attack_choice == 1:
            return self.razor_sharp_claws(), "Razor-Sharp Claws"
        elif attack_choice == 2:
            return self.fangs_of_death(), "Fangs of Death"
        elif attack_choice == 3:
            return self.lick_wounds(), "Lick Wounds"
        else:
            return 0, "Invalid Attack"

    def razor_sharp_claws(self):
        hit_chance = self.d20.roll()
        if hit_chance >= 13:
            return sum(self.d6.roll() for _ in range(2))
        else:
            print("Razar claws misses!")
            return 0

    def fangs_of_death(self):
        hit_chance = self.d20.roll()
        if hit_chance >= 16:
            return sum(self.d6.roll() for _ in range(3))
        else:
            print("Fangs of Death misses!")
            return 0

    def lick_wounds(self):
        heal_amount = self.d6.roll()
        self.hp = min(self.hp + heal_amount, self.max_hp) # min funciton, used example from class to do this
        print(f"The Mugwump licks its wounds and heals for {heal_amount} points!")
        return -heal_amount