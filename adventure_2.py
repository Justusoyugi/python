import os
os.system('cls' if os.name == 'nt' else 'clear')


print("================================================== WELCOME ==================================================")
print("\n\t-->You wake up to the sound of a scream and look aroundto see a full moon above you. Ravens fly past as a mist rolls in. In the distance you hear church bells toll. Around you tombstones stretch as far as your eyes can see. You don't know how you got into this graveyard - but you want to go home. There are two paths in front of you. One is dark and overgrown and appears to lead to a big, vine-covered crypt. The other path is flanked by stone angels and you can hear singing off-key. Which path do you choose?")

while True:
    a1 = input(
        "\n->Type angel to go down the angel path OR crypt to go down the crypt path: ").lower().strip()

    if a1 == "angel":
        print("\n\t-->As you walk closer to the angels' faces, you see they're all distorted. You get into a clearing and see a little girl screaming “help me!” as a hooded figure approaches her with a hook and a sharp-nailed hand reaches out at her. Out of the corner of your eye you see a shovel. Picking up the shovel, in your loudest voice you shout: “Stop! I have a shovel and I'm not afraid to use it!” The hooded figure lets out a ghastly scream as you bring the sharp side of the shovel onto the hooded figure's head. A satisfying CRACK rings out and the hooded figure disappears in a puff of smoke. You look at the little girl only to find she has glowing red eyes and she begins walking toward you laughing and saying “come play with me”. Looking around you see the back door to a church with a glowing green light coming out. Do you:")
        while True:
            a2 = input(
                "\n->Type stay to stay and talk to the little girl OR go to go into the creepy church: ").lower().strip()

            if a2 == "stay":
                print("\n\t-->The little girl walks slowly towards you. She is calling out in a creepy voice “play with me. Play with me” Suddenly she grabs you by the hand. Then she starts to choke you. She whispers in your ears “I'm going to make you bones.” All you can see is her glowing red eyes as you fall to the ground. You feel around desperately on the ground and manage to grab a large stick. You can hardly breathe, but you find the strength to hit the girl on the side of the head. She lets go of you and slumps on top of you. You push her dead body off you and sit up. You see an angel slowly flying towards you. The angel says “I need your help to rescue the other children.")
                while True:
                    a3 = input(
                        "\n->Type help to stay and help the angel OR run to run away: ").lower().strip()

                    if a3 == "help":
                        print("\n\t-->The angel tells you sadly: “An evil demon has trapped all the children from the village inside the old church. They're his slaves and he makes them catch other children for him. “We must find the magic key hidden in one of the statues” You start to run quickly around the statues, but you cannot see anything. “Hurry!” cries the angel “they are coming for you.” You turn around quickly and fall over one of the statues and see a strange glowing ball among the leaves. Behind you, you hear footsteps and many children crying. “Pick up the ball” yells the angel. “It is the key.” You grab the ball and suddenly you hear in your head a voice whispering the spell to you. “Make it glow, let them go” You say the spell over and over. There is a big flash of light like a rainbow and the children all wake up from the spell. The angel says “You've done it, you have saved them!” The children run to you and put you on their shoulders. “Thank you, thank you, we can go home now.” The angel flies ahead and all the children follow carrying you home.")
                        print("THE END")
                        break
                    elif a3 == "run":
                        print("\n\t-->You run away from the angel slowly because your leg is broken. Up ahead you see a grey shape covered with spider webs. As you get closer you see it is a machine. A sign next to it says GHOST VACUUM. You decide to help the angel and run back to it. You see zombies fighting the angel and the angel says “Help me!” You turn on the ghost vacuum and it makes a growling noise. You hold the tube out and suck up all the zombies. The angel says thank you and teleports you home.")
                        print("THE END")
                        break
                    else:
                        print("Please type help or run: ")
                break

            elif a2 == "go":
                print("\n\t-->The little girl's eyes remind you of burning embers. You turn and run as she slowly advances. But as you leave you hear the little girl's voice turn distorted and creepy. “Don't leave me! Don't go!” You check behind your back and can still hear her yelling but she is no more in sight. You suddenly hit something solid and land on the ground. Dazed from impact the voices have stopped. You see you have collided with a building of peculiar features. At first glance it looks eerily translucent but your head says otherwise. You see a stone angel again on either side of the doorway. What is with these creepy figures? You decide to go in. As you walk through the door a green light immediately blinds you (temporarily). Your eyes adjust to the light and to your amazement you see a ball of green light floating above a medieval-looking bowl. The green light illuminates the words behind it. “Those who break the silent sound in this cemetery are forever bound.” Should you:")
                while True:
                    a4 = input(
                        "\n->Type leave to leave because it's really creepy in here OR work out to work out what those words mean: ").lower().strip()

                    if a4 == "leave":
                        print("\n\t-->You decide to leave. It's too creepy in here with all that green light. You turn around but someone's blocking your exit. Before long it dawns on you it's the figure that attacked the little girl. You bash him on the head with your trusty shovel. A line of curses ring out from under the hood. The figure to your surprise pulls his hood back.A normal face appears, to your relief. A thin-lipped man says: “What are you doing here? Leave immediately!” You say “Which way's out?” He leads you to a path. You walk down the path and look back to find the figure gone. Before long, you reach the cemetery gates. You look back, and everything seems normal. “Huh?” you exclaim. It's the same boring graveyard you come to every Sunday. Where are the angels? Where is the mist? You are curious to find out what happened but don't feel like dying. You go home.")
                        print("THE END")
                        break
                    elif a4 == "work out":
                        print("\n\t-->You decide to stay after all. You're already here, right? “Those who break this silent sound, in this cemetery are\ orever bound.” You repeat it in your head, but nothing comes to mind. You take a step back and accidently step on a hidden button. “WHAT?” you exclaim, looking down on what you've stepped on. You wait for something to happen. Three minutes pass by and you shrug, deciding it must be false. You turn and pass the door to look at another inscription, then something catches your attention. Weren't there 2 stone angels outside? You look again, they're gone. How could that happen? You turn around and come face to face with a demonic face. It was the angel you stepped back. “NO” You say and step away. The 2 angels have come to life and they've begun chanting “THOSE WHO BREAK THE SILENT SOUND, IN THIS CEMETERY ARE FOREVER BOUND.” The angelic one faces YOU and says something that scares you more than the demonic angel ever could. “You're not leaving after all that, this is the end”. Everything goes black…")
                        print("THE END")
                        break
                    else:
                        print("Please type leave or work out: ")
                break
            else:
                print("Please type stay or go:")
        break

    elif a1 == "crypt":
        print("\n\t-->You walk down into the crypt. You look around and see a shadow on the ground, something that looks like a white face with dark eyes. A shriek sounds in the air. You look around and you see nothing. You start running as fast as you can, your heart pounding rapidly. Suddenly a large distorted figure appears two feet in front of you. Shocked, your feet slip over something slimy and you plummet to the ground. You hear a sound behind you. Looking back you see a Reaper dressed in a long black satin robe, who grabs you by the neck and drags you into a stone building. You feel cold and see candles placed in each corner of the room and a pile of skulls on the ground. The Reaper stands opposite holding an axe. An open door stands next to you.")
        while True:
            a5 = input(
                "\n->Type fight to fight OR flight if your fear takes over and your feet take flight: ").lower().strip()

            if a5 == "fight":
                print("\n\t-->You realise that the axe is actually a fasce* and pick it up and strike the Reaper on the eyeball and the heart. The Reaper explodes in a mushroom cloud of souls and bones. While celebrating your victory you stumble on a skull. How do you die?")
                while True:
                    a6 = input("\n->Type floor if  you think it's on the floor covered in blood OR type bone if you think it's a bone sticking out of a brain OR rare if you think it's Pneumonoultramicroscopicsilicovolcanoconiosis: ").lower().strip()

                    if a6 == "floor":
                        print(
                            "\n\t-->You trip over a log and in the middle there is a pointy stick and if you trip over that you will die easily. And you do. ")
                        print("THE END")
                        break
                    elif a6 == "bone":
                        print("\n\t-->You stumble on a skull with a bone sticking out of the brain. It is poking your heart. Blood is covering you. The vampires come and suck all your blood.")
                        print("THE END")
                        break

                    elif a6 == "rare":
                        print("\n\t-->You stumble upon a discarded skull and the passing ash from the explosion travels into your mouth. Gasping for air, the ash enters into your lungs and you tragically die. Your rotting corpse lies there lifeless on the infertile soil of the miserable graveyard, patiently awaiting the gravediggers who will soon dispose of you deep in the earth. ")
                        print("THE END")
                        break

                    else:
                        print("Please type floor, bone or rare: ")
                break

            elif a5 == "flight":
                print("\n\t-->You choose to run away because you felt extremely scared. You exit the door in the distance and you see an old rusty plane. You get into the plane and start the engine. The engine rattles as if it is going to explode. Looking out you see the Reaper pacing towards you. Quickly you pull the throttle and the aircraft begins rolling. The Reaper's eyes grow wide as the plane begins picking up speed. He runs but is no match for the plane's speed and in the next instant you hear a crunch and the windscreen turns red and you cannot see ahead of you. You push the windscreen wiper button. Nothing happens. Do you?")

                while True:
                    a7 = input(
                        "\n->Type stop to try and stop the plane OR continue to continue to fly OR dance to dance on top of the plane: ").lower().strip()

                    if a7 == "stop":
                        print("\n\t-->The plane continues running. You can't see anything in front of you. You hear some crashing sounds underneath the plane. You feel scared and try to pull the brakes. But the gears get stuck and suddenly the plane ends up plunging off the edge of a cliff. You start running towards the back of the plane but it's TOO LATE. The plane rolls down the cliff and explodes. You die")
                        print("THE END")
                        break

                    elif a7 == "continue":
                        print("\n\t-->You continue flying. There is no way you are going back to that hellish place. Beads of sweat are forming on your forehead as you squint through the red bloody remains of the Reaper. You grip the steering wheel tightly and with your heart punching through your chest you pick up altitude: 100m, 200m, 300m, 400m, 500m. As the plane speeds up the red layer begins dispersing and you vaguely see a thundercloud looming in the distance. You head towards it in the hope the moisture will wash off the dead matter. You slowly close your eyes as you enter into the gigantic mass. An ear-piercing roar of thunder sounds but you daren't open your eyes. 10 minutes pass with your eyelids clamped shut. Finally, you have the courage to slowly open your eyes. A blue clearing stretches across the windscreen and a sense of relief sweeps through you as you see little cotton clouds in the sky. Now, time to go home.")
                        print("THE END")
                        break

                    elif a7 == "dance":
                        print("\n\t-->You don't know what to do, so, as a famous man once said: “When in trouble, start dancing”. So you put the plane on automatic pilot, and open the emergency release door. You climb, climb, climb. Soon you're at the top of the plane dancing. Suddenly rainclouds come rolling in and KAKABOOM! You're struck by lightning. Lucky you're a robot, so you survive. Then you fall off from the impact for a day, because the plane happened to be a spaceplane, just like Hephaestus (google it). Then you land with only your toe broken because luckily you're made of titanium. You see you're in a human settlement, your programming tells you to destroy all humans you meet, make robot factories to churn out other terminators like yourself, and destroy the human race. FIVE YEARS LATER The robot uprising has been successful and you go back to where you were created, in the graveyard, but OH NO IT IS RAINING. The water gets into your circuits and you begin to MA-mal-mallllfunccctionnn-DOES NOT COMPUTE 00111010100110011010100110101010101010001111 00000101201001010101010101001111")
                        print("THE END")
                        break

                    else:
                        print("Please type stop, dance or continue: ")
                break

            else:
                print("Please type fight or flight: ")
        break
    else:
        print("Please type angel or crypt: ")
