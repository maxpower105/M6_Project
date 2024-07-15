from die_Ziller import Die
from Player_Ziller import Character


# I did warrior first so a lot was copied over

class SociallyAwkwardComputerEngineeringUndergradStudent(Character):
    def __init__(self):
        super().__init__('Socially Awkward Computer Engineering Undergrad Student', [Die(12) for _ in range(4)])  # pull in name and hp
        self.d4 = Die(4)
        self.d6 = Die(6)
        self.d10 = Die(10)
        self.charging_magic = False  # Add this for 4th attack

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
            return 4  # Thunder   # Add this for 4th attack
        else:
            return 3  # recharge

    def attack(self, ai_controlled=False):
        if ai_controlled:
            attack_choice = self.__ai()

            # Add this for 4th attack, this line is really importatn, this is how we go from charging ot attacking
        elif self.charging_magic:  # this checks to see if charging is set to true, then thunder attack
            self.charging_magic = False  # This resets the charging function back to false
            return self.magic(), "Magic! Test Test"  # Execute thunder attack if true
        else:
            print("How would you like to attack?")
            print("1. Make Eye Contact")
            print("2. Nerd Rage")
            print("3. Anime Cosplay Heal")
            print('4. Magic The Gathering Super Fan Attack (two turn attack)')  # Add this for 4th attack
            attack_choice = int(input("Enter choice: "))

        # added third choice for healing
        if attack_choice == 1:
            return self.eye_contact(), "TESTS Stab Hertz - Eye Contact"
        elif attack_choice == 2:
            return self.nerd_rage(), "TESTSLighining - Nerd rage"
        elif attack_choice == 3:
            self.cosplay_heal()
            return 0, "Recharge"
        elif attack_choice == 4:
            self.magic_the_gathering_charge()  # Add this for 4th attack
            return 0, "MTG Thunder Charging"  # need ot retunr 0 so damage attack result has a value
        else:
            return 0, "test Invalid Attack"

    def eye_contact(self):
        hit_chance = self.d20.roll()
        if hit_chance >= 16:  # 25% chance
            return sum(self.d4.roll() for _ in range(10))
        else:
            print("stab hertz misses!")
            return 0

    def nerd_rage(self):
        hit_chance = self.d20.roll()
        if hit_chance >= 6:  # 75% chance
            return sum(self.d4.roll() for _ in range(1))
        else:
            print("Shock misses!")
            return 0

    def cosplay_heal(self):
        heal_amount = sum(self.d6.roll() for _ in range(3))
        self.hp = min(self.hp + heal_amount, self.max_hp)  # min function, used example from class to do this
        print(f"Recharges for {heal_amount} points!")

    def magic_the_gathering_charge(self):  #Add this for 4th attack
        self.charging_magic = True
        print("Reddy Kilowatt is charging Thunder!")

    def magic(self):  # Add this for 4th attack
        charge = self.d20.roll() * 3
        hit_chance = self.d20.roll()
        if hit_chance >= 18:  #18:  # 15% chance
            return sum(self.d10.roll() for _ in range(1)) + charge
        else:
            print("Thunder misses")
            return 0
