from secrets import choice
import time
import random
from urllib import response


def print_pause(message_to_print):  # determine time delay
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):  # validate input of player
    while True:
        response = input(prompt).lower()
        if response == option1:
            break
        elif response == option2:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def begin_game():       # player starts game
    print_pause("Long ago in a distant land.\n")
    print_pause("An enemy unleashed an unspeakable evil.\n")
    print_pause("But a brave warrier wielding the greatest weapon " +
                "bestowed on humanity stepped forth to oppose him.\n")
    print_pause("To defend yourself, you will have to fight.\n")


def choose_weapon():  # choose a weapon at random
    response = valid_input("Choose your weapon." +
                           "Enter 1/2?\n", "1", "2").lower()
    response = random.choice(["1", "2"])

    if "1" in response:
        print_pause("A wand!!! Great choice! Now let's cook up a fire spell\n")
        print_pause("EXPENSIVE PETROLATUM!!\n")

    elif "2" in response:
        print_pause("A kitana! Nice!\n")
        print_pause("The evil you have caused my" +
                    "people is enough!!! Aaaarrgghhhhhh\n")

    else:
        print_pause("Invalid response!\n")
    end_game()


def end_game():  # End game
    print_pause("Yay! You land a hit! the enemy retreats into darkness\n")
    print_pause("But before he disappears you make a final decision.\n")

    response = valid_input("How would you like to proceed" +
                           " Warrior? (Enter 1 or 2)\n", "1", "2").lower()
    response = random.choice(["1", "2"])

    if response == "1":
        print_pause("You decide to leave the enemy and" +
                    "forgive him for all evil caused.\n")
        print_pause("Just then, he tackles you and swoops you" +
                    "into a worm hole.\n")
        print_pause("You disintegrate slowly... GAME OVER!\n")

    elif response == "2":
        print_pause("You corner him and land a fatal hit!\n")
        print_pause("The enemy cries out and curses you " +
                    "with his dying breath\n")
        print_pause("He dies and your people are saved. YOU WIN!!!\n")

    else:
        print_pause("Sorry, You have to make a choice.\n")
    play_again()


def play_again():  # play again
    response = valid_input("Want to play again? (yes/no)\n",
                           "no", "yes").lower()
    if "no" in response:
        print_pause("Too bad... See you next time!\n")

    elif "yes" in response:
        print_pause("Let's begin!\n")
        game()


def game():
    begin_game()
    choose_weapon()


game()
