import random


def instructions():
    print(r"""
How to play Dice:

- Roll the die.
- Your opponent then rolls their die.
- Whoever has the highest number wins.
- Rinse and repeat.
       """)


def intro():
    response = input("\nPress ENTER to continue...\n")

    if response == "":
        play()

    else:
        print("You typed some text before enter, why on earth would you do" +
              " this???\n")
        intro()


def play():
    response = input("To roll your die, input 'roll'. To quit, input 'quit'." +
                     " If you need help, input 'help'.\n")

    if response == 'roll':
        dieroll1 = random.randint(1, 6)
        dieroll2 = random.randint(1, 6)
        print(f"You rolled a {dieroll1}. Your opponent rolled a {dieroll2}.\n")

        if dieroll1 > dieroll2:
            print("You win. Congrats.\n")
            intro()

        elif dieroll1 < dieroll2:
            print("Great job buddy. You managed to lose the worlds simplest " +
                  "game.\n")
            intro()

        elif dieroll1 == dieroll2:
            print("Whoa! You both rolled the same thing.\n")
            play()

    elif response == 'quit':
        response = input("Are you really sure you want to leave? (yes / no)\n")

        if response == 'yes':
            print("Okay fine.\n")
            quit()

        elif response == 'no':
            print("Great. Glad to see you've got nothing better to do.\n")

        else:
            print("I didn't understand that, so I'll assume you want to play" +
                  " some more dice.\n")
            play()

    elif response == 'help':
        instructions()
        response = input("Input anything to go back.\n")

        if response == '':
            play()

        else:
            play()

    else:
        print("I didn't understand that.\n")
        play()


instructions()
intro()
