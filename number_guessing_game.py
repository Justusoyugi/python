import random
import os
os.system('cls' if os.name == 'nt' else 'clear')

number = random.randint(1, 100)
count = 0
prompt = input("Do you want to play a game?(yes/no) ")
if prompt == "yes".lower():
    name = input("Please enter your name: ")
    print(f"Hello {name}, welcome to the number guessing game.\n You have the chance to guess the correct number between 1-100 with as few tries as possible.\n Good luck and let's go.!")
    while True:
        try:
            guess = int(input("Guess a number: "))

            count += 1
            if guess == number:
                print(
                    f"🎉✨ Congratulations, you guessed the number in {count} tries.")
                break
            elif guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

elif prompt == "no".lower():
    print("😒 Goodbye")

else:
    print("❌ Invaid choice")
