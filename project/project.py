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

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    win_choices = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    computer_choice = choices[random.randrange(0, 2, 1)]

    while True:
        user_choice = input("Enter rock, paper, or scissors: ")
        if user_choice in choices:
            break
        else:
            print(f"{user_choice} is not a valid choice")

    print(f"You chose {user_choice}")
    print(f"Opponent chose {computer_choice}")

    if win_choices[user_choice] == computer_choice:
        print("Win")
    elif win_choices[computer_choice] == user_choice:
        print("Lose")
    else:
        print("Tie")

if __name__ == "__main__":
    rock_paper_scissors()