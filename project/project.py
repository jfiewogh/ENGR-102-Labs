# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Project
# Date: 27 October 2026

import random

red = "\033[31m"
blue = "\033[34m"
magenta = "\033[95m"
end = "\033[0m"

def concat_strings_by_line(first: str, second: str, sep="", first_start="", first_end="", second_start="", second_end="") -> str:
    first_lines = first.split("\n")
    second_lines = second.split("\n")
    return "\n".join([
        first_start + first_lines[i] + first_end + sep + second_start + second_lines[i] + second_end 
        for i in range(min(len(first_lines), len(second_lines)))
    ])

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    win_choices = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    ascii_art = {
        "rock": {
            "right": "    _______  \n---'   ____) \n      (_____)\n      (_____)\n      (____) \n---.__(___)  ",
            "left":  "  _______    \n (____   '---\n(_____)      \n(_____)      \n (____)      \n  (___)__.---"
        },
        "paper": {
            "right": "    _______       \n---'   ____)____  \n          ______) \n          _______)\n         _______) \n---.__________)   ",
            "left":  "       _______    \n  ____(____   '---\n (______          \n(_______          \n (_______         \n   (__________.---"
        },
        "scissors": {
            "right": "    _______       \n---'   ____)____  \n          ______) \n       __________)\n      (____)      \n---.__(___)       ",
            "left":  "       _______    \n  ____(____   '---\n (______          \n(__________       \n      (____)      \n       (___)__.---"
        }
    }

    wins, losses, ties, total = 0, 0, 0, 0

    while True:
        # Get user choice
        while True:
            user_choice = input("Enter rock, paper, or scissors (or \"exit\" to exit): ")
            if user_choice == "exit":
                return
            if user_choice in choices:
                break
            else:
                print(f"{user_choice} is not a valid choice")

        # Get computer choice
        computer_choice = random.choice(choices)

        # Output choices in ascii art
        print(concat_strings_by_line(
            ascii_art[user_choice]["right"], 
            ascii_art[computer_choice]["left"], 
            "    ", 
            first_start=red, first_end=end, second_start=blue, second_end=end))

        # Determine and output result
        if win_choices[user_choice] == computer_choice:
            wins += 1
            print(f"{red}You won! Opponent chose {computer_choice}.{end}")
        elif win_choices[computer_choice] == user_choice:
            losses += 1
            print(f"{blue}You lost! Opponent chose {computer_choice}.{end}")
        else:
            ties += 1
            print(f"{magenta}Tie! Both chose {user_choice}.{end}")
        total += 1

        print(f"{red}Wins: {wins} ({wins / total * 100:.1f}%){end} | {blue}Losses: {losses} ({losses / total * 100:.1f}%){end} | {magenta}Ties: {ties} ({ties / total * 100:.1f}%){end} | Total: {total}")

        # Ask user if they want to try again
        while True:
            restart_input = input("Would you like to try again (Y/N)? ")
            if restart_input in "Yy":
                break
            elif restart_input in "Nn":
                return

def tic_tac_toe():
    ...
    # Create game here

def hangman():
    from math import *
letter_dictionary = {"a":"A", "b":"B", "c":"C", "d":"D", "e":"E", "f":"F", "g":"G", "h":"H", "i":"I", "j":"J", "k":"K", "l":"L", "m":"M", "n":"N","o":"O", "p":"P", "q":"Q", "r":"R", "s":"S", "t":"T", "u":"U", "v":"V", "w":"W", "x":"X", "y":"Y", "z":"Z", "A":"A", "B":"B", "C":"C", "C":"D", "E":"E", "F":"F", "G":"G", "H":"H", "I":"I", "J":"J", "K":"K", "L":"L", "M":"M", "N":"N", "O":"O", "P":"P", "Q":"Q", "R":"R", "S":"S", "T":"T", "U":"U", "V":"V", "W":"W", "X":"X", "Y":"Y", "Z":"Z", " ": " "}
new_hidden_word = ""
invalid = 1
current_word = ""
guess = ""
while True:
    while invalid == 1:
        hidden_word = input("Enter the hidden word: ")
        for letter in hidden_word:
            if letter in letter_dictionary:
                new_hidden_word += letter_dictionary[letter]
                invalid = 0
            else:
                print("That is not a valid word. Try Again.")
                hidden_word = ""
                invalid = 1
                break
    number_of_letters = len(new_hidden_word)
    for i in range(number_of_letters):
        if i != " ":
            current_word += "_"
        else:
            current_word += " "
    while invalid == 0:
        guess = input("Enter a guess for the hidden word: ")
        if guess in letter_dictionary:
            new_guess = letter_dictionary[guess]
    if guess == "exit":
        f
#Call function to end the game 
    if guess == "restart":
        True
    
    ...
    # Create game here

def print_menu(menu_games):
    for key, value in menu_games.items():
        print(f"{key}. {value["name"]}")

if __name__ == "__main__":
    menu_games = {
        "1": {"name": "rock paper scissors", "function": rock_paper_scissors},
        "2": {"name": "tic-tac-toe", "function": tic_tac_toe},
        "3": {"name": "hangman", "function": hangman}
    }

    while True:
        print_menu(menu_games)
        choice = input("Enter choice from menu: ")
        if choice in menu_games:
            print()
            menu_games[choice]["function"]()
        else:
            print(f"{choice} is not a valid choice")
        print()
