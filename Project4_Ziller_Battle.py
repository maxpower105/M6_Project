# MSOE CSC-5120-301
# Project 6
# Benjamin Shaske, Walter Ziller
# 6.20.2024

# Software Used
# Python V3.12.3
# PyCharm V2024.1.1 (Community)
# PyTest V8.2.2
# ----------------------------------------------------------------------------------------------------------------------

from die_Ziller import Die
from Player_Ziller import Character
from mugwump_Ziller import Mugwump
from Warrior_Ziller import Warrior
from Reddy_Kilowatt import Reddy_Kilowatt
from SACEUS import SociallyAwkwardComputerEngineeringUndergradStudent


def initial_menu():
    print("\n1. Create a new character")
    print("2. Load a character from a save file")
    select_flag = False
    choice = '0'
    while not select_flag:
        choice = input("Enter choice: ")
        if choice.isdigit() and int(choice) == 1:
            select_flag = True
        elif choice.isdigit() and int(choice) == 2:
            select_flag = True
        else:
            print('\nNot a valid input')
    if int(choice) == 1:
        return create_new_character()
    elif int(choice) == 2:
        return load_character_from_file()
    else:
        print("\nInvalid choice. Please try again.")
        return initial_menu()


def create_new_character():
    # Choose player character
    print("\nChoose your character:")
    print("1. Warrior")
    print("2. Mugwump")
    print("3. Reddy Kilowatt")
    print("4. Socially Awkward Computer Engineering Undergrad Student")
    select_flag = False
    while not select_flag:
        player_choice = input("Enter choice: ")
        if (player_choice.isdigit() and int(player_choice) == 1) \
                or (player_choice.isdigit() and int(player_choice) == 2) \
                or (player_choice.isdigit() and int(player_choice) == 3) \
                or (player_choice.isdigit() and int(player_choice) == 4):
            select_flag = True
        else:
            print('\nNot a valid input')
    print()

    # Ask user for nickname
    nickname = input("Enter a nickname for your character: ")

    # basic boolean output based on user choice, added line for AI portion
    if int(player_choice) == 1:
        player = Warrior()
        player_ai = False
    elif int(player_choice) == 2:
        player = Mugwump()
        player_ai = False
    elif int(player_choice) == 3:
        player = Reddy_Kilowatt()
        player_ai = False
    elif int(player_choice) == 4:
        player = SociallyAwkwardComputerEngineeringUndergradStudent()
        player_ai = False
    else:
        print("Invalid choice. Please try again.")
        return create_new_character()
    # Assign nickname ot be hte new name
    player.name = nickname
    return player, player_ai


def load_character_from_file():
    filename = input("Enter the filename of the save file (no extension, e.g., 'warrior_save'): ") + ".json"
    try:
        player = Character.load_from_json(filename)  # Asking the file to be the player
        player_ai = False  # Assuming loaded characters are controlled by the player
        return player, player_ai
    except (FileNotFoundError, ValueError) as e:  # error handler if they type the name wrong, or it's not there
        print(f"Error loading character: {e}")
        return initial_menu()  # GO back to initialize menu


# This selects who goes first
def initiative():
    d10 = Die(10)  # Load 10 sided die
    player_initiative = d10.roll()  # player roll
    opponent_initiative = d10.roll()  # opponent roll
    while player_initiative == opponent_initiative:
        player_initiative = d10.roll()
        opponent_initiative = d10.roll()
    # Have it return boolean value for easy determination in later battle sequence
    if player_initiative > opponent_initiative:
        return 1  # player goes first
    else:
        return 2  # opponent goes first


# This determines victor
def victory(victor, player, opponent):  # pass in victor, player, and opponent, so it can be used outside this function
    if victor == player.name:  # Changed name to whatever player chose to be
        print(
            f"\nThe citizens cheer and invite you back to town for a feast as thanks for saving their lives against "
            f"the {opponent.name}!")
    else:
        print(
            f"\nYou lose to the {opponent.name}! He mocks you for how pathetically you fought")  # Load in opponent
        # name here if you lose

    save_choice = input("Do you want to save your character? (yes/no): ").strip().lower()
    if save_choice in ["y", "yes", "Yes", "Y"]:  # Follow instruction exactly as asked in lab description
        save_filename = input("Enter the filename to save your character (without extension): ").strip() + '.json'
        player.save_to_json(save_filename)

    else:
        return False


# This is how to initiate play again sequence, basic user input returning T or F
def playAgain():
    choice = input("\nWould you like to play again (yes/no)? ")  # User input function
    if choice in ["y", "yes", "Yes", "Y"]:  # Follow instruction exactly as asked in lab description
        return True
    else:
        print("\nGame Over. Thanks for playing")
        return False


# This where most of important play actually happens, lots of changes had to be done when super class added
def battle(player, opponent,player_ai):  # Pass in player, opponent, and player_ai. Player_ai was added so that warrior and mugwump can
    # play as AI.
    cur_initiative = initiative()  # each round the first attacker will be selected by the initiate function, set to
    # variable so it can be called later in the function

    if cur_initiative == 1:  # pulling boolean value from initiative function
        print(f"\n{player.name} attacks first!")  # change this to include f string for whatever player selected
        attack_result = player.attack(ai_controlled=player_ai)  # this pulls in the info returned from the attack
        # function called in the  warrior
        # or mugwump characters
        # Where first value is hte damage amount and the second value is the attack name
        # return self.attack_with_sword(), "Trusty Sword" from this line for example
        damage = attack_result[0]  # first item returned is the damage
        attack_name = attack_result[1]  # second item is the attack name
        # this pulls in the info returned from the attack function called in the  warrior or mugwump characters
        opponent.take_damage(damage)  # after attack performed this calls take damage method to reduce the hp
        # Print out of the sequence that just happened with the names changed to f strings to be flexible
        print(f"{player.name} attacks with {attack_name}!")
        print(f"{player.name} deals {damage} points of damage to {opponent.name}!")
        print(f"\n{player.name} HP: {player.get_hitpoints()}, {opponent.name} HP: {opponent.get_hitpoints()}")

        # this set victor at end of first turn of the round
        if opponent.get_hitpoints() <= 0:
            return player.name
        # this is how the opponent does damage, added code so its AI controlled, set to true here
        attack_result = opponent.attack(ai_controlled=True)
        damage = attack_result[0]  # Access the first element of the tuple
        attack_name = attack_result[1]
        # damage, attack_name = opponent.attack(ai_controlled=True)
        # had to use if statement to deal with fact mugwump can heal
        if damage > 0:
            # take damage info
            player.take_damage(damage)
            # Printout of what happened with take damage
            print(f"\n{opponent.name} attacks with {attack_name}!")
            print(f"{opponent.name} deals {damage} points of damage to {player.name}!")
        # this logic is specific to mugwump, not used for warrior
        elif damage < 0:
            print(f"\n{opponent.name} heals for {-damage} points!")
        # final report out for the round
        print(f"\n{player.name} HP: {player.get_hitpoints()}, {opponent.name} HP: {opponent.get_hitpoints()}")

        # this sets name of victor at end of this turn
        if player.get_hitpoints() <= 0:
            return opponent.name
    # This is if the opponent goes first, basically same code just in a different order. opponent first then player
    else:
        print(f"\nThe {opponent.name} attacks first!")

        attack_result = opponent.attack(ai_controlled=True)
        damage = attack_result[0]
        attack_name = attack_result[1]

        if damage > 0:
            player.take_damage(damage)
            print(f"{opponent.name} attacks with {attack_name}!")
            print(f"{opponent.name} deals {damage} points of damage to {player.name}!")
        elif damage < 0:
            print(f"{opponent.name} heals for {-damage} points!")

        print(f"\n{player.name} HP: {player.get_hitpoints()}, {opponent.name} HP: {opponent.get_hitpoints()}")

        if player.get_hitpoints() <= 0:
            return opponent.name
        attack_result = player.attack(ai_controlled=player_ai)  # this pulls in the info returned from the attack
        # function called in the  warrior or mugwump characters
        # return self.attack_with_sword(), "Trusty Sword" from this line for example
        damage = attack_result[0]  # first item returned is the damage
        attack_name = attack_result[1]  # second
        opponent.take_damage(damage)
        print(f"\n{player.name} attacks with {attack_name}!")
        print(f"{player.name} deals {damage} points of damage to {opponent.name}!")
        print(f"\n{player.name} HP: {player.get_hitpoints()}, {opponent.name} HP: {opponent.get_hitpoints()}")

        if opponent.get_hitpoints() <= 0:
            return player.name

    return "none"  # this is here so that the play again sequence will work correctly, default is none if nobody
    # has =< 0 hp


# main function
def main():
    play_again = True  # sets play again to true right away, later this can be changed based on battle sequence results
    while play_again:  # welcome message
        print("\n===============================  Welcome to Battle Simulator 3001! ==================================")
        print("•You may choose to fight as a Valiant Warrior defending your humble village from an evil Mugwump!")
        print("•Or fight as a snarling Mugwump and take down the pathetic Warrior")
        print("•\n•But don't forget about the lesser known heroes; "
              "\n•\tReady Kilowatt and the Socially Awkward Computer Engineering Undergrad Student!")
        print("•\n•Choose wisely, and let the epic battle begin!")
        print("=====================================================================================================")
        player, player_ai = initial_menu()

        # Choose opponent character, same code as first time asked
        print("\nChoose your opponent:")
        print("1. Warrior")
        print("2. Mugwump")
        print("3. Reddy Kilowatt")
        print("4. Socially Awkward Computer Engineering Undergrad Student")
        select_flag = False
        while not select_flag:
            opponent_choice = input("Enter choice: ")
            if (opponent_choice.isdigit() and int(opponent_choice) == 1) \
                    or (opponent_choice.isdigit() and int(opponent_choice) == 2) \
                    or (opponent_choice.isdigit() and int(opponent_choice) == 3) \
                    or (opponent_choice.isdigit() and int(opponent_choice) == 4):
                select_flag = True
            else:
                print("\nInvalid choice. Please try again.")
        print()

        # Created if statement to handle when player selects their character other is AI controlled, using boolean value
        if int(opponent_choice) == 1:
            opponent = Warrior()
        elif int(opponent_choice) == 2:
            opponent = Mugwump()
        elif int(opponent_choice) == 3:
            opponent = Reddy_Kilowatt()
        elif int(opponent_choice) == 4:
            opponent = SociallyAwkwardComputerEngineeringUndergradStudent()

        else:
            print(
                "Invalid choice, defaulting to Mugwump.")  # handles if user doesn't enter selection correctly, default
            # is mugwump like OG program
            opponent = Mugwump()

        # Victor determination done in these lines
        victor = "none"  # set variable to none

        # Show the initial HP and Battle Opponents
        print(f"======================================= LET THE BATTLE BEGIN! =======================================\n"
              f"{player.name} HP: {player.get_hitpoints()} VS. {opponent.name} HP: {opponent.get_hitpoints()}")

        while victor == "none":  # While statement so it keep looking after each round
            victor = battle(player, opponent, player_ai)  # battle function goes through each round, if battle isn't
            # decided returns none,
            # otherwise returns player or opponent
        # once loop exits the victory function will call the winner form the player or opponent, see code above
        victory(victor, player, opponent)

        # # SAve to file
        # player.save_to_json(f'{player.name.lower()}_save.json')

        # Call play again function once done
        play_again = playAgain()


if __name__ == "__main__":
    main()
