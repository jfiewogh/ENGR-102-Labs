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



def tic_tac_toe() :
    
    def print_board(board) :
        print("\n")
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")
        print("\n")
    board = [" " for _ in range(9)] # testing the print_board function
    # print_board(board) # testing the print_board function
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
        if board[0] == board[4] == board[8] == player :
            return True
        if board[2] == board[4] == board[6] == player :
            return True
        return False
    def play_game() :
        board = [" " for _ in range(9)]
        current_player = "X"
        moves_played = 0
        
        print("Welcome to Tic-Tac-Toe!")
        
        while True :
            print_board(board)
            move = (input(f"Player {current_player}, enter your move (1-9): ")) - 1
            
            if move == "exit":
                    return
           
            # check that input is valid
            if int(move) not in range(1,10):
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            move = int(move) - 1  # Convert to 0-based index

            # check that spot is not taken
            if board[move] != " " :
                print("That spot is already taken. Please try again.")
                continue    

            # Place mark and move foward
            board[move] = current_player
            moves_played += 1
            
            # Check for winner or tie
            if check_winner(board, current_player) :
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if moves_played == 9 :
                print_board(board)
                print("It's a tie!")
                break

            # switch turns
            current_player = "X" if current_player == "O" else "X"

        # ask to play again  
        while True:
            restart_input = input("Would you like to try again (Y/N)? ")

            if restart_input in "Yy":
                return True
            elif restart_input in "Nn":
                return False
    # Keep playing until the user decided to stop 
    while play_game() :
        pass


def hangman():
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
