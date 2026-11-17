from math import *

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
            hidden_word = " ".join(input("Enter the hidden word or phrase: ").upper().strip().split())
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
                
hangman()