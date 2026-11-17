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
    while True:
        board = [str(i) for i in range(1, 10)]

        current_player = red + "X" + end
        moves_played = 0
        
        print("Welcome to Tic-Tac-Toe!")
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

def hangman():
# define all variables and functions for code
    letter_dictionary = {"a":"A", "b":"B", "c":"C", "d":"D", "e":"E", "f":"F", "g":"G", "h":"H", "i":"I", "j":"J", "k":"K", "l":"L", "m":"M", "n":"N","o":"O", "p":"P", "q":"Q", "r":"R", "s":"S", "t":"T", "u":"U", "v":"V", "w":"W", "x":"X", "y":"Y", "z":"Z", "A":"A", "B":"B", "C":"C", "C":"D", "E":"E", "F":"F", "G":"G", "H":"H", "I":"I", "J":"J", "K":"K", "L":"L", "M":"M", "N":"N", "O":"O", "P":"P", "Q":"Q", "R":"R", "S":"S", "T":"T", "U":"U", "V":"V", "W":"W", "X":"X", "Y":"Y", "Z":"Z", " ": " "}
    new_hidden_word = ""
    invalid = 1
    current_word = ""
    guess = ""
    guesses = []
    incorrect_guesses = []
    correct_guesses = []
    number_of_incorrect_guesses = 0
    # Checks guess if it is a letter and in the hidden word. Adds it to the list of guesses, checks if there is a win or loss, and continues the guess loop if there still needs to be more guesses. Adds it to incorrect guesses if incorrect. 
    def check_guesses_letters(a):
        for i in hidden_word:
            if guess in hidden_word:
                guess = current_word[i]
                correct_guesses.append(guess)
            else:
                incorrect_guesses.append(guess)
                number_of_incorrect_guesses += 1
        if current_word == hidden_word:
            invalid = 1
        elif number_of_incorrect_guesses == 7:
            invalid = 2
        print(current_word)
        print(f"Your correct guesses are {correct_guesses}, and your incorrect guesses are {incorrect_guesses}")
    # Checks guess if it is a complete word and exactly = the hiddden word. Adds it to the list of guesses, checks if there is a win or loss, and continues the guess loop if there still needs to be more guesses. Adds it to incorrect guesses if incorrect. 
    def check_guesses_words(a):
        if guess == hidden_word:
            current_word = guess
            invalid = 1
        else:
            incorrect_guesses.append(guess)
            number_of_incorrect_guesses += 1
        if number_of_incorrect_guesses == 7:
            invalid = 2
        print(current_word)
        print(f"Your correct guesses are {correct_guesses}, and your incorrect guesses are {incorrect_guesses}")
    # Game loop is a while true loop
    while True:
        # Take input for hidden word and check if it is valid
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
        # make the hidden word into the current word that will be displayed to the player
        number_of_letters = len(new_hidden_word)
        for i in range(number_of_letters):
            if i != " ":
                current_word += "_"
            else:
                current_word += " "
        # Take input for guesses and check if it is valid or if they want to exit or restart
        while invalid == 0:
            guess = input("Enter a guess for the hidden word: ")
            if guess in letter_dictionary:
                new_guess = letter_dictionary[guess]
            if guess == "exit":
                f
        #Call function to end the game 
            if guess == "restart":
                True
            if guess == "exit":
                True
            if len(guess) == 1:
                if guess in letter_dictionary:
                    guess = letter_dictionary[guess]
                    if guess in guesses:
                        print("Already guessed. Try again.")
                        invalid == 0
                        continue
                    else: 
                        check_guesses_letters(letters)
                        guesses.append(guess)
                        print(f"Your guesses are {guesses}.")
                        check_guesses_letters(guess)
                        # function returns invalid value. If it is a win, invalid = 1, if it is a loss invalid = 2, and if the game has to continue invalid = 0
                else:
                    print("Guess not valid. Try again.")
                    continue
            else: 
                for i in guess:
                    if i in letter_dictionary:
                            guess = letter_dictionary[guess]
                            check_guesses_words(words) 
                            if guess in guesses:  
                                print("Already guessed. Try again.")
                                invalid == 0
                                continue 
                            else: 
                                guesses.append(guess)
                                print(f"Your guesses are {guesses}.")
                            check_guesses_words(guess)
                            # function returns invalid value. If it is a win, invalid = 1, if it is a loss invalid = 2, and if the game has to continue invalid = 0
                    else:
                        print("Guess not valid. Try again.")
                        invalid == 0
                        continue
        parts_to_hangman = {
                "1" : " O ",
                "3" : "|",
                "5" : " | ",
                "4" : "\ ",
                "2" : "/",
                "7" : "\ ",
                "6" : "/",}
        number_of_incorrect_guesses = 0
        incorrect_guesses = []
        max_incorrect_guesses = 7

        def display_hangman(number_of_incorrect_guesses, guess, word) :

            if guess not in word :
                number_of_incorrect_guesses += 1
                incorrect_guesses.append(guess)
                
                if number_of_incorrect_guesses == 1 :
                    print("", parts_to_hangman["1"])
                    print(f"Incorrect! You have {max_incorrect_guesses - number_of_incorrect_guesses} guesses left.")

                elif number_of_incorrect_guesses == 2 :
                    print("", parts_to_hangman["1"],"\n", parts_to_hangman["2"])
                    print(f"Incorrect! You have {max_incorrect_guesses - number_of_incorrect_guesses} guesses left.")

                elif number_of_incorrect_guesses == 3 :
                    print("", parts_to_hangman["1"],"\n", parts_to_hangman["2"] + parts_to_hangman["3"])
                    print(f"Incorrect! You have {max_incorrect_guesses - number_of_incorrect_guesses} guesses left.")

                elif number_of_incorrect_guesses == 4 :
                    print("", parts_to_hangman["1"],"\n", parts_to_hangman["2"] + parts_to_hangman["3"] + parts_to_hangman["4"])
                    print(f"Incorrect! You have {max_incorrect_guesses - number_of_incorrect_guesses} guesses left.")

                elif number_of_incorrect_guesses == 5 :
                    print("", parts_to_hangman["1"],"\n", parts_to_hangman["2"] + parts_to_hangman["3"] + parts_to_hangman["4"],"\n", parts_to_hangman["5"])
                    print(f"Incorrect! You have {max_incorrect_guesses - number_of_incorrect_guesses} guesses left.")

                elif number_of_incorrect_guesses == 6 :
                    print("", parts_to_hangman["1"],"\n", parts_to_hangman["2"] + parts_to_hangman["3"] + parts_to_hangman["4"],"\n", parts_to_hangman["5"], "\n", parts_to_hangman["6"])
                    print(f"Incorrect! You have {max_incorrect_guesses - number_of_incorrect_guesses} guesses left.")

                elif number_of_incorrect_guesses == 7 :
                    print("", parts_to_hangman["1"],"\n", parts_to_hangman["2"] + parts_to_hangman["3"] + parts_to_hangman["4"],"\n", parts_to_hangman["5"], "\n", parts_to_hangman["6"], parts_to_hangman["7"])
                    print("Game Over! You've been hanged!")

        # print("", parts_to_hangman["1"],"\n", parts_to_hangman["2"] + parts_to_hangman["3"] + parts_to_hangman["4"],"\n", parts_to_hangman["5"], "\n", parts_to_hangman["6"], parts_to_hangman["7"]) # testing first disp;ay for hangman


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
            print(f"\"{choice}\" is not a valid choice")
        print()