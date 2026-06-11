import os
os.system('cls' if os.name == 'nt' else 'clear')

print("======Welcome to this adventure.========")
title = ("The mystery of the lost planet")
print(title.upper())
print("*** You are the commander of the starship Apex. Your radar picks up an unusual energy signature on an uncharted, misty planet below.\n You only have enough fuel for one landing.")
print("•	Do you land your ship in the glowing forest? 🌲🌲")
print("•	Do you land near the mysterious, metallic ruins? 🕳️")
while True:
    answer = input(
        "-> Type forest to land in the glowing forest OR ruins to land near the mysterious metallic ruins: ").lower().strip()
    if answer == "forest":
        print("*** You land in the glowing forest. The trees have bioluminescent leaves that cast an eerie blue light.\nSuddenly, a pack of tiny, floating creatures surrounds your ship. \nThey don't look dangerous, but they are chewing on your wiring!")
        print("•	Do you try to shoot them away with a loud warning shot? 🔫")
        print("•	Do you offer them your emergency food rations to calm them down? 🍔")
        while True:
            answer2 = input(
                "-> Type shoot to shoot them away OR food to offer them your emergency food rations: ").lower().strip()
            if answer2 == "shoot":
                print("The warning shot startles the creatures, but it also angers them. They emit a piercing shriek that destroys your ship's engine.\nYou are now stranded on the planet forever.")
                print("THE END!!💀")
                break
            elif answer2 == "food":
                print("The floating creatures love your rations! They chew happily and leave your wiring alone. In return, they guide you to a hidden crystal that can power your ship for a thousand years. You blast off into space a hero!")
                print("THE END!!VICTORY🎉🎉✨")
                break
            else:
                print("Please type shoot or food.")
        break
    elif answer == "ruins":
        print("*** You land near the metallic ruins. The ground is made of shifting, black sand. As you step out of the ship, a giant mechanical door in the ruins slowly creaks open, revealing a dark, spiraling staircase.")
        print("•	Do you draw your laser blaster and walk inside? 🤺")
        print("•	Do you turn back, leave the ruins, and explore the forest instead? 🚶‍♂️")
        while True:
            answer3 = input(
                "-> Type laser blaster to draw it and walk inside OR turn back to leave the ruins and explore the forest instead: ").lower().strip()
            if answer3 == "laser blaster":
                print("You walk down the dark staircase. At the bottom, you find an ancient AI computer that holds the secrets to the universe.\nHowever, because your blaster is drawn, the computer perceives you as a threat and traps you in a forcefield forever.")
                print("THE END!!💀")
                break
            elif answer3 == "turn back":
                print("*** You land in the glowing forest. The trees have bioluminescent leaves that cast an eerie blue light.\nSuddenly, a pack of tiny, floating creatures surrounds your ship. \nThey don't look dangerous, but they are chewing on your wiring!")
                print("•	Do you try to shoot them away with a loud warning shot? 🔫")
                print(
                    "•	Do you offer them your emergency food rations to calm them down? 🍔")
                while True:
                    answer2 = input(
                        "-> Type shoot to shoot them away OR food to offer them your emergency food rations: ").lower().strip()
                    if answer2 == "shoot":
                        print("The warning shot startles the creatures, but it also angers them. They emit a piercing shriek that destroys your ship's engine.\nYou are now stranded on the planet forever.")
                        print("THE END!!💀")
                        break
                    elif answer2 == "food":
                        print("The floating creatures love your rations! They chew happily and leave your wiring alone. In return, they guide you to a hidden crystal that can power your ship for a thousand years. You blast off into space a hero!")
                        print("THE END!!VICTORY🎉🎉✨")
                        break
                    else:
                        print("Please type shoot or food.")
                break
            else:
                print("Please type laser blaster or turn back")
        break
    else:
        print("Please type forest or ruins: ")
