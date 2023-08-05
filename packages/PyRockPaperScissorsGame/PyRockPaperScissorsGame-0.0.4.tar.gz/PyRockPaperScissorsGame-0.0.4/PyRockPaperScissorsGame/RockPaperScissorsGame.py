from termcolor import colored
import random


def Rock_Paper_Scissors():
    game_array = ["r", "p", "s"]
    comp_wins = 0
    user_wins = 0
    print()
    print("Welcome to the Rock, Paper, Scissors game!")
    print()
    print("Characters list:")
    print("Rock - sound like the Rock, input 'r'")
    print("Paper - light but strong tool for destroying a rock, input 'p'")
    print("Scissors - can cut the paper (so strong), input 's'")
    print()

    while user_wins != 3 and comp_wins != 3:
        user_choice = input("Your pick >>>")
        print()
        comp_choice = random.choice(game_array)
        # loop for beautiful output of comp_choice
        if comp_choice == "r":
            cool_comp_choice = "Rock"
        elif comp_choice == "p":
            cool_comp_choice = "Paper"
        else:
            cool_comp_choice = "Scissors"
        # loop for cool output of user_choice
        if user_choice == "r":
            cool_user_choice = "Rock"
        elif user_choice == "p":
            cool_user_choice = "Paper"
        elif user_choice == "s":
            cool_user_choice = "Scissors"
        else:
            cool_user_choice = "I am incorrect sign"
        print(f"Your sign: {cool_user_choice}, Computer sign: {cool_comp_choice}")
        # main loop
        if user_choice == "r":
            if comp_choice == "r":
                print(colored("Tie", "blue"))
            elif comp_choice == "p":
                print(colored("You lose this round", "red"))
                comp_wins += 1
            elif comp_choice == "s":
                print(colored("You win this round", "green"))
                user_wins += 1
        elif user_choice == "p":
            if comp_choice == "p":
                print(colored("Tie", "blue"))
            elif comp_choice == "s":
                print(colored("You lose this round", "red"))
                comp_wins += 1
            elif comp_choice == "r":
                print(colored("You win this round", "green"))
                user_wins += 1
            else:
                print("You inputted a wrong character")
        # if scissors
        elif user_choice == "s":
            if comp_choice == "s":
                print(colored("Tie", "blue"))
            elif comp_choice == "r":
                print(colored("You lose this round", "red"))
                comp_wins += 1
            elif comp_choice == "p":
                print(colored("You win this round", "green"))
                user_wins += 1
            else:
                print("You inputted a wrong character")
        else:
            print(colored("You inputted a wrong character", "magenta"))

        print(f"User wins: {user_wins}, Computer wins: {comp_wins}")
        print()
    if comp_wins == 3:
        print(colored("Computer win((( Good luck next time!", "red"))
        print()
    else:
        print(colored("You win!!! Well done!)))xD)", "green"))
        print()