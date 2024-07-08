# MSOE CSC-5120-301
# Project 4
# Benjamin Shaske
# 6.20.2024

# Software Used
# Python V3.12.3
# PyCharm V2024.1.1 (Community)
# PyTest V8.2.2
# ----------------------------------------------------------------------------------------------------------------------

"""Import Relevant files"""
import shaskeb4_character
from shaskeb4_dice import Die

"""Create an alias for ease of coding"""
bfs = shaskeb4_character  # bfs, prefix for individual project 4 files.

"""
 BattleSim Driver for Battle Simulator 3000
 You may need to set the Python interpreter if you have an error along the top. Choose local, and it should find it
"""

"""
     # we need to create a Ten-sided die to be used for checking initiative
"""
d10 = Die(10)


def main():  # not testable

    # sentinel value for the game loop
    keep_playing = True

    while keep_playing:
        # print the introduction and rules
        intro()
        numPlayers = playerSelect()

        if int(numPlayers) == 1:
            Player1 = characterSelect()
            Player2 = aiCharacterSelect()
        else:
            Player1 = characterSelect()
            Player2 = characterSelect()

        victor = "none"  # Flag set for continuous battle sim play until a victor is defined.

        # while neither combatant has lost all of their hit points, report status and battle!
        while victor == "none":
            report(Player1, Player2)
            victor = battle(Player1, Player2)

            # declare the winner
            if (victor != "none"):  # one of them has won
                report(Player1, Player2)
                victory(Player1, Player2, victor)
                # ask to play again
                keep_playing = playAgain()

    # Thank the user for playing your game
    print("\nThank you for playing Battle Simulator 3001!")


"""
   This method displays the introduction to the game and gives a description of the rules.
 """


def intro():  # not testable
    # Write a suitable introduction to your game
    print("\n---------------------------------------------------------------------------------------------------------"
          "\n--------------------------------Welcome to Battle Simulator 3001!----------------------------------------"
          "\n--------------------------- The world's more low tech battle simulator!----------------------------------"
          "\nYou will choose to be a Valiant Warrior defending your humble village from an evil Mugwump; or, choose"
          "\nthe Mugwump and attempt to eat the citizens of the town for dinner after vanquishing their valiant"
          "\nprotector!\nIf you choose the Warrior, you will have your Trusty Sword, which deals decent damage, but"
          "\ncan be tough to hit with sometimes. You also have your Shield of Light, which is not as strong as your"
          "\nsword, but is easier to deal damage with.\n If you choose the Mugwump, you will choose to attack your"
          "\nvictims with razor sharp claws or fangs of death. Or maybe use the Mugwump's magical healing lick!"
          "\n----------------------------------Let the epic battle begin!---------------------------------------------"
          "\n----------------------------------------Fight bravely!---------------------------------------------------"
          "\n---------------------------------------------------------------------------------------------------------")


"""
   This method handles the battle logic for the game.
   @param warrior The Warrior of Light!
   @param mugwump The Evil Mugwump!
   @return The name of the victor, or "none", if the battle is still raging on
 """


def battle(Player1, Player2):  # not testable?
    # determine who attacks first (Roll! For! Initiative!) and store the result
    cur_inititive = initiative()  # this a 1 or 2
    # attack code
    # If Player 1 attacks first
    if (cur_inititive == 1):  # Player 1 attackes first
        # Player 1 attacks and assigns the resulting damage to Player 2.
        print("Player 1 attacks first!")
        cur_attack = Player1.attackChoice()
        damage = Player1.attack((cur_attack))  #calculate damage caused by warrior
        #Player2.takeDamage(damage) # apply damage to Player 2
        if (damage > 0):
            Player2.takeDamage(damage)
        elif isinstance(Player1, bfs.Mugwump):  # Check for mugwump
            Player1.takeDamage(damage)  # healing because it is negative

        if (Player1.hitPoints == 0):
            return "Player 2 Wins!"  # Player: 2 wins!

        # Check if the Mugwump has been defeated
        if (Player2.hitPoints <= 0):
            return "Player 1 Wins!"

        # If not, Player 2 attacks!
        print("\nPlayer 2's attacks back!")
        cur_attack = Player2.attackChoice()
        damage = Player2.attack((cur_attack))  # calculate damage caused by warrior

        # the mugwump may have healed itself, so have to check
        if (damage > 0):
            Player1.takeDamage(damage)
        elif isinstance(Player2, bfs.Mugwump):  # Check for mugwump
            Player2.takeDamage(damage)  # healing because it is negative

        if (Player1.hitPoints == 0):
            return "Player 2 Wins!"  # Player 2 wins!
    else:
        print("Player 2 attacks first!")
        cur_attack = Player2.attackChoice()
        damage = Player2.attack((cur_attack))  # calculate damage caused by warrior
        # Player2.takeDamage(damage) # apply damage to Player 2
        if (damage > 0):
            Player1.takeDamage(damage)
        elif isinstance(Player2, bfs.Mugwump):  # Check for mugwump
            Player2.takeDamage(damage)  # healing because it is negative

        if (Player2.hitPoints == 0):
            return "Player 1 Wins!"  # Player: 2 wins!

        # Check if the Mugwump has been defeated
        if (Player1.hitPoints <= 0):
            return "Player 2 Wins!"

        # If not, Player 2 attacks!
        print("\nPlayer 1 attacks back!")
        cur_attack = Player1.attackChoice()
        damage = Player1.attack((cur_attack))  # calculate damage caused by warrior

        # the mugwump may have healed itself, so have to check
        if (damage > 0):
            Player2.takeDamage(damage)
        elif isinstance(Player1, bfs.Mugwump):  # Check for mugwump
            Player1.takeDamage(damage)  # healing because it is negative

        if (Player2.hitPoints == 0):
            return "Player 1 Wins!"  # Player 2 wins!
    #else: # mugwump attacks first!

    # If neither combatant is defeated, the battle rages on!
    return "none"


"""
   This method reports the status of the combatants
   @param warrior The Warrior of Light!
   @param mugwump The Evil Mugwump!
 """


def report(Player1, Player2):  # not testable
    if isinstance(Player1, bfs.Warrior):
        print(f"\nPlayer 1's Warrior HP: {Player1.hitPoints}")
    else:
        print(f"\nPlayer 1's Mugwump HP: {Player1.hitPoints}")
    if isinstance(Player2, bfs.Warrior):
        print(f"Player 2's Warrior HP: {Player2.hitPoints}\n")
    else:
        print(f"Player 2's Mugwump HP: {Player2.hitPoints}\n")


"""
   Determines which combatant attacks first and returns the result. In the case of a tie,
   re-roll.
   @return 1 if the warrior goes first, 2 if the mugwump goes first
 """


# this has randomness, how can we test it? Can we set a seed for the random number generator?
def initiative() -> int:  # return 1 for Player 1, 2 for Player 2
    # roll for initiative for both Players
    # until one initiative is greater than the other
    Player1_initiative = d10.roll()
    Player2_initiative = d10.roll()
    while (Player1_initiative == Player2_initiative):
        Player1_initiative = d10.roll()
        Player2_initiative = d10.roll()

    if (Player1_initiative > Player2_initiative):
        return 1  # Player 1 goes first
    else:
        return 2  # Player 2 goes first


"""
   This method declares the victor of the epic battle
   @param victor the name of the victor of the epic battle
 """


def victory(Player1, Player2, victor):  # not testable (or at least we won't worry about testing it)
    if (victor == "Player 1 Wins!"):
        if isinstance(Player1, bfs.Warrior):
            print(f"\nPlayer 1 WINS!\nPlayer 1's Warrior has victoriously defended the village!\n"
                  f"The people will sleep good in their beds and tell stories of this glorious battle!")
        else:
            print(f"\nPlayer 1 WINS!\nPlayer 1's Mugwump has slaughtered it's enemy! The land will forever fear the "
                  f"Mugwumps!")

    else:
        if isinstance(Player2, bfs.Warrior):
            print(f"\nPlayer 2 WINS!\nPlayer 2's Warrior has victoriously defended the village!\n"
                  f"The people will sleep good in their beds and tell stories of this glorious battle!")
        else:
            print(f"\nPlayer 2 WINS!\nPlayer 2's Mugwump has slaughtered it's enemy! The land will forever fear the "
                  f"Mugwumps!")


"""
    This function is to determine the player selection criteria.
"""


def playerSelect():
    print('\nSelect number of players: Enter 1 or 2\n1 - One Player\n2 - Two Players')
    valid_input = False
    while not valid_input: # While loop to validate input
        numPlayerSelect = input()
        if numPlayerSelect.isdigit() and (int(numPlayerSelect) == 1 or int(numPlayerSelect) == 2):
            valid_input = True
            return numPlayerSelect
        else:
            print('Not a valid input. Please Select number of players:\n1 - One Player\n2 - Two Players')

"""
    This function is to determine player character selection.
"""
def characterSelect():
    print('\nEnter 1 for Warrior or 2 for Mugwump\n1 - Warrior\n2 - Mugwump')
    valid_input = False
    while not valid_input:
        charSelect = input()
        if charSelect.isdigit() and (int(charSelect) == 1 or int(charSelect) == 2):
            print(
                'Select character control method. (User or AI)\n1 - User controller character\n'
                '2 - AI controlled character.')
            aiSelect = input()
            if aiSelect.isdigit() and (int(aiSelect) == 1 or int(aiSelect) == 2):
                if int(charSelect) == 1:
                    if int(aiSelect) == 1:
                        Player = bfs.Warrior(False)
                        valid_input = True
                    else:
                        Player = bfs.Warrior(True)
                        valid_input = True
                else:
                    if int(aiSelect) == 1:
                        Player = bfs.Mugwump(False)
                        valid_input = True
                    else:
                        Player = bfs.Mugwump(True)
                        valid_input = True
            else:
                print(
                    'Not a valid input. Please enter a 1 for user controller character or 2 for AI controlled '
                    'character')
        else:
            print('Not a valid input. Please enter a 1 for Warrior or 2 for Mugwump.')
    return Player

"""
    This function is to select a random character for the computer AI.
"""
def aiCharacterSelect():
    d100 = Die(100)
    roll = d100.roll()
    # Use a d100 die to help with 50-50 odds of character generation. Selected d100 for future customization of odds.
    if (roll <= 50):  # 50-50 odds
        # Select Warrior class
        Player = bfs.Warrior(True)
    else:
        # Select Mugwump class
        Player = bfs.Mugwump(True)

    return Player


"""
   This method asks the user if they would like to play again
   @param in Scanner
   @return true if yes, false otherwise
 """


def playAgain() -> bool:
    choice = input("Would you like to play again (yes/no)?")
    if (str.lower(choice) == "y" or str.lower(choice) == "yes"):
        return True
    return False


if __name__ == "__main__":
    main()
