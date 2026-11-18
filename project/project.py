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
from math import *
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

    print("Welcome to Rock Paper Scissors!")

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

def print_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(board, player) : 
    # Check rows
    for i in range(0, 9, 3) :
        if board[i] == board[i + 1] == board[i + 2] == player :
            return True
    # Check columns
    for i in range(3) :
        if board[i] == board[i + 3] == board[i + 6] == player :
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")

    while True:
        board = [str(i) for i in range(1, 10)]

        current_player = red + "X" + end
        moves_played = 0
        
        print_board(board)
        
        while True:
            # Get move from user
            while True:
                move = input(f"Player {current_player}, enter your move (1-9) (or \"exit\" to exit): ")
                if move == "exit":
                    return
                # Check if that input is valid
                if move in "123456789" and move != "":
                    move_index = int(move) - 1
                else:
                    print("Invalid input. Please enter a number between 1 and 9, inclusive.")
                    continue
                # Check if that spot is not taken
                if board[move_index] in "123456789":
                    break   
                else:
                    print("That spot is already taken. Please try again.")

            # Place mark and move foward
            board[move_index] = current_player
            moves_played += 1

            print_board(board)

            # Check for winner
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            # Check for tie
            if moves_played == 9:
                print("It's a tie!")
                break

            # Switch turns
            if current_player == blue + "O" + end:
                current_player = red + "X" + end
            else:
                current_player = blue + "O" + end

        # Ask user if they want to try again
        while True:
            restart_input = input("Would you like to try again (Y/N)? ")
            if restart_input in "Yy":
                break
            elif restart_input in "Nn":
                return

def char_is_valid(char):
    return char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def guess_is_valid(guess):
    return guess in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def guess_in_hidden_word(guess, hidden_word):
    return guess in hidden_word

def display_hangman(num_incorrect_guesses):
    hangman_parts = ["O", "/", "|", "\\", "/", "\\"]
    parts = [" "] * 6
    for i in range(num_incorrect_guesses):
        parts[i] = hangman_parts[i]
    print(f"  +---+  \n  |   |  \n  {parts[0]}   |  \n {parts[1]}{parts[2]}{parts[3]}  |  \n {parts[4]} {parts[5]}  |  \n      |  \n=========")

def get_current_word(correct_guesses: list[str], hidden_word: str) -> str:
    current_word = ""
    for letter in hidden_word:
        if letter in correct_guesses:
            current_word += letter
        elif letter == " ":
            current_word += " "
        else:
            current_word += "_"
    return current_word

def hangman():
    max_incorrect = 6

    print("Welcome to Hangman!")

    # Game loop is a while true loop
    while True:
        # Initialize variables
        guesses = []
        incorrect_guesses = []
        correct_guesses = []

        # Take input for hidden word and check if it is valid
        while True:
            hidden_word = " ".join(input("Enter the hidden word or phrase (or \"exit\" to exit): ").upper().strip().split())
            if hidden_word == "EXIT":
                return
            if hidden_word != "" and all([char_is_valid(letter) for letter in hidden_word]):
                hidden_word = hidden_word.upper()
                break
            print("That is not a valid word. Try again.")
        print("\n" * 100)

        # Guess loop
        while True:
            # Take input for guesses and check if it is valid or if they want to exit or restart
            while True:
                guess = input("Enter a guess for the hidden word (or \"exit\" to exit): ")

                if guess == "exit":
                    return            
                if len(guess) != 1:
                    print("Guess be exactly one letter. Try again.")
                    continue

                guess = guess.upper()

                # Check if guess is valid
                if not guess_is_valid(guess):
                    print("Guess is invalid. Try again.")
                    continue
                if guess in guesses:
                    print("Already guessed. Try again.")
                    continue

                # We have a valid guess
                guesses.append(guess)
                break

            # Check if guess is correct
            guess_is_correct = guess_in_hidden_word(guess, hidden_word)
            if guess_is_correct:
                correct_guesses.append(guess)
            else:
                incorrect_guesses.append(guess)
                print(f"Incorrect! You have {max_incorrect - len(incorrect_guesses)} incorrect guesses left.")

            # Display hangman
            display_hangman(len(incorrect_guesses))

            # Get current word
            current_word = get_current_word(correct_guesses, hidden_word)
            print(current_word)

            # Output guesses
            print(f"Your correct guesses are {correct_guesses}, and your incorrect guesses are {incorrect_guesses}.")
            print(f"Your guesses are {guesses}.")        
            print()

            # Check for win
            if current_word == hidden_word:
                print("You won the game!")
                break
            # Check for loss
            if len(incorrect_guesses) == max_incorrect:
                print("Game over! You've been hanged!")
                break

        # Ask user if they want to try again
        while True:
            restart_input = input("Would you like to try again (Y/N)? ")
            if restart_input in "Yy":
                print()
                break
            elif restart_input in "Nn":
                return

def print_menu(menu_games):
    for key, value in menu_games.items():
        print(f"{key}: {value["name"]}")

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
            print(f"\"{choice}\" is not a valid choice")
        print()