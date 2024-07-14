from die_Ziller import Die
from Player_Ziller import Character
from mugwump_Ziller import Mugwump
from Warrior_Ziller import Warrior
from Reddy_Kilowatt import Reddy_Kilowatt
def initial_menu():
    print("1. Create a new character")
    print("2. Load a character from a save file")
    choice = int(input("Enter choice: "))

    if choice == 1:
        return create_new_character()
    elif choice == 2:
        return load_character_from_file()
    else:
        print("Invalid choice. Please try again.")
        return initial_menu()

def create_new_character():
    # Choose player character
    print("Choose your character:")
    print("1. Warrior")
    print("2. Mugwump")
    print("3. Reddy Kilowatt")
    player_choice = int(input("Enter choice: "))

    # Ask user for nickname
    nickname = input("Enter a nickname for your character: ")

    # basic boolean output based on user choice, added line for ai portion
    if player_choice == 1:
        player = Warrior()
        player_ai = False
    elif player_choice == 2:
        player = Mugwump()
        player_ai = False
    elif player_choice == 3:
        player = Reddy_Kilowatt()
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
        player = Character.load_from_json(filename) # Assing the file to be the player
        player_ai = False  # Assuming loaded characters are controlled by the player
        return player, player_ai
    except (FileNotFoundError, ValueError) as e: # error handler if they type the name wrong or its not there
        print(f"Error loading character: {e}")
        return initial_menu() # GO back to initlize menu

# This selects who goes first
def initiative(): 
    d10 = Die(10) # Load 10 sided die
    player_initiative = d10.roll() # player roll
    opponent_initiative = d10.roll() # opponent roll
    while (player_initiative == opponent_initiative):
        player_initiative = d10.roll()
        opponent_initiative = d10.roll()
    # Have it returna boolean value for easy determination in later battle sequence
    if player_initiative > opponent_initiative:
        return 1  # player goes first
    else:
        return 2  # opponent goes first

# This determines victor
def victory(victor, player, opponent): # pass in victor, player, and opponent so it can be used outside this function
    if victor == player.name: # Changed name to whatever player chose to be
        print(f"The citizens cheer and invite you back to town for a feast as thanks for saving their lives against the {opponent.name}!")
    else:
        print(f"You lose to the {opponent.name}! He mocks you for how pathetically you fought") # Load in opponent name here if you lose

    save_choice = input("Do you want to save your character? (yes/no): ").strip().lower()
    if save_choice in ["y", "yes", "Yes", "Y"]: # Follow instruction exaclty as asked in lab description
        save_filename = input("Enter the filename to save your character (without extension): ").strip() + '.json'
        player.save_to_json(save_filename)

    else:
        return False
# This is how to initiate play again sequesnce, basic user input returning T or F
def playAgain():
    choice = input("Would you like to play again (yes/no)? ") # User input fucntion
    if choice in ["y", "yes", "Yes", "Y"]: # Follow instruction exaclty as asked in lab description
        return True
    else:
        print("Game Over. Thanks for playing")
        return False

# This where most of important play actually happens, lots of changes had to be done when super class added
def battle(player, opponent, player_ai): # Pass in player, opponent, and player_ai ( player_ai was added so that warrior and mugwamp can play as ai)
    cur_initiative = initiative() # each round the first attacker will be selected by the intiate function, set to variable so it can be called later in the funciton
    
    if cur_initiative == 1: # pulling boolean value from intiative function
        print(f"The {player.name} attacks first!") # change this to include f string for whatever player selected
        attack_result = player.attack(ai_controlled=player_ai) # this pulls in the info retunred from the attack function called in the  warrior or mugwamp characters
        # Where first value is hte damage amount and the second value is the attack name
        # return self.attack_with_sword(), "Trusty Sword" from this line for example
        damage = attack_result[0] # first item retunred is the damage
        attack_name = attack_result[1] # second item is the attack name
        # this pulls in the info retunred from the attack function called in the  warrior or mugwamp characters
        opponent.take_damage(damage) # after attack performed this calls take damage nethod to reduce the hp
        # Print out of the the sequence that just happened with the names changed to f strings to be flexible
        print(f"{player.name} attacks with {attack_name}!")
        print(f"{player.name} deals {damage} points of damage to {opponent.name}!")
        print(f"{player.name} HP: {player.get_hitpoints()}, {opponent.name} HP: {opponent.get_hitpoints()}")
        
        # this set victor at end of first turn of the round
        if opponent.get_hitpoints() <= 0:
            return player.name
        # this is how the oppoent does damage, added code so its ai controlled, set to true here
        attack_result = opponent.attack(ai_controlled=True)
        damage = attack_result[0]  # Access the first element of the tuple
        attack_name = attack_result[1]
        # damage, attack_name = opponent.attack(ai_controlled=True)
        # had to use if statemtn to deal with fact mugwamp can heal
        if damage > 0:
            # take damage info
            player.take_damage(damage)
            # Printout of what happened with take damage
            print(f"{opponent.name} attacks with {attack_name}!")
            print(f"{opponent.name} deals {damage} points of damage to {player.name}!")
        # this logic is specific to mugwamp, not used for warrior
        elif damage < 0:
            print(f"{opponent.name} heals for {-damage} points!")
        # final report out for the round
        print(f"{player.name} HP: {player.get_hitpoints()}, {opponent.name} HP: {opponent.get_hitpoints()}")
        
        # this sets name of voctor at end of this turn
        if player.get_hitpoints() <= 0:
            return opponent.name
    # THis is if the opponent goes first, basically same code just in a different order. opponent first then player
    else:
        print(f"The {opponent.name} attacks first!")
        
        attack_result = opponent.attack(ai_controlled=True)
        damage = attack_result[0]  
        attack_name = attack_result[1]
        
        if damage > 0:
            player.take_damage(damage)
            print(f"{opponent.name} attacks with {attack_name}!")
            print(f"{opponent.name} deals {damage} points of damage to {player.name}!")
        elif damage < 0:
            print(f"{opponent.name} heals for {-damage} points!")

        print(f"{player.name} HP: {player.get_hitpoints()}, {opponent.name} HP: {opponent.get_hitpoints()}")
        
        if player.get_hitpoints() <= 0:
            return opponent.name
        attack_result = player.attack(ai_controlled=player_ai) # this pulls in the info retunred from the attack function called in the  warrior or mugwamp characters 
        # return self.attack_with_sword(), "Trusty Sword" from this line for example
        damage = attack_result[0] # first item retunred is the damage
        attack_name = attack_result[1] # second
        opponent.take_damage(damage)
        print(f"{player.name} attacks with {attack_name}!")
        print(f"{player.name} deals {damage} points of damage to {opponent.name}!")
        print(f"{player.name} HP: {player.get_hitpoints()}, {opponent.name} HP: {opponent.get_hitpoints()}")
        
        if opponent.get_hitpoints() <= 0:
            return player.name

    return "none" # this is here so that the play again sequence will work correctly, default is none if nobody has =< 0 hp

#main function
def main():
    play_again = True # sets play again to true right away, later this can be changed based on battle sequence results
    while play_again: # welcome message
        print("Welcome to Battle Simulator 3001!")
        print("You may choose to fight as a Valiant Warrior defending your humble village from an evil Mugwump!")
        print("Or fight as a snarling Mugwamp and take down teh pathetic Warrior")
        print("\n Choose wisely, and let the epic battle begin!\n")
        player, player_ai = initial_menu()


        # Choose opponent character, same code as forst time asked
        print("Choose your opponent:")
        print("1. Warrior")
        print("2. Mugwump")
        print("3. Reddy Kilowatt")
        opponent_choice = int(input("Enter choice: "))
        
        # Created if statement to handle when player selects their character other is ai controlled, using boolean value
        if opponent_choice == 1:
            opponent = Warrior()
        elif opponent_choice == 2:
            opponent = Mugwump()
        elif opponent_choice == 3:
            opponent = Reddy_Kilowatt()
        else:
            print("Invalid choice, defaulting to Mugwump.") # handles if user doesnt enter selction correctly, default is mugwamp like OG program
            opponent = Mugwump()
            
        # Victor determinintaion done in these lines    
        victor = "none" # set variable to none
        while victor == "none": # While satement so it keep looking after each round
            victor = battle(player, opponent, player_ai) # battle function goes through each round, if battle isnt decided returns none, otherwise retunrs player or opponent
        # once loop exits the victory function will call the winner form the player or opponent, see code above
        victory(victor, player, opponent)

        # # SAve to file
        # player.save_to_json(f'{player.name.lower()}_save.json')

        # Call play again function once done
        play_again = playAgain()

if __name__ == "__main__":
    main()
