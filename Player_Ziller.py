from die_Ziller import Die

# Creation of the super class to handle 
# added the common items from the diagram shown in UML
# Functions had similar code in class examples, just modified slightly to be in super class
class Character:
    def __init__(self, name, hp_dice): # this class will determine the name and starting hp, starting hp will be finally determined in each character with a die roll
        self.d20 = Die(20)
        self.hp_dice = hp_dice
        self.hp = 0
        self.max_hp = 0
        self.name = name
        self.set_initial_hitpoints()

    def set_initial_hitpoints(self): # setting intial hitpoints
        self.hp = sum(die.roll() for die in self.hp_dice)
        self.max_hp = self.hp

    def get_hitpoints(self):
        return self.hp

    def take_damage(self, damage): # general take damage maths
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack(self):
        return 0, "None"  # To be overridden in subclasses of warrior or mugwamp


















