import random

def dice_roll():
    return random.randint(1, 6) #Returns a Randome number between 1 and 6.

def dice_game():
    print("Welcome to the Dice Roll Game:")
    print("Instructions:")
    print("First we randomly select your roll value.")
    print("Then we randomly select the computer's roll value.")
    print("The bigger roll wins!")
    print("Let's Begin!")

    input("\nPress Enter to get your roll value.")
    player_roll = dice_roll()
    print(f"Your Roll value is {player_roll}.")

    input("\nPress Enter to get the Computer's roll value.")
    comp_roll = dice_roll()
    print(f"The computer's Roll value is {comp_roll}.")

    if player_roll > comp_roll: #Condition for winning.
        print("\nCongratulations! You Win!")
    elif player_roll < comp_roll: #Condition for losing.
        print("\nSorry, You Lost.")
    else:
        print("\nIt's a DRAW!")

if __name__ == "__main__":
    dice_game()

while True:
    reset = input("\nType 'reset' to play again or press Enter to exit.\n").lower()
    if reset == "reset":
        dice_game() #Calls the function dice_game to repeat the proces.
    else:
        print("Goodbye!")
        break
