import random
import os
os.system('cls' if os.name == 'nt' else 'clear')

# count number of times the dice has been rolled
count = 0
# Loop
while True:
    # Ask if they want to roll the dice.
    choice = input("Would you like to roll a dice?(yes/no) ")

    # If yes, generate two random numbers
    if choice == "yes".lower():
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You rolled a {die1} and a {die2}")
        count += 1
    # If no, exit the game
    elif choice == "no".lower():
        print("Thank you for playing.")
        print(f"You rolled the dice {count} times.")
        break
    # else ,invalid choice
    else:
        print("Invalid choice!")
