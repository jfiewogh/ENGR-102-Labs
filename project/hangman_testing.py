from math import *

# Checks guess if it is a letter and in the hidden word. Adds it to the list of guesses, checks if there is a win or loss, and continues the guess loop if there still needs to be more guesses. Adds it to incorrect guesses if incorrect. 
def check_guesses_letters(guess, hidden_word):
    return guess in hidden_word


parts_to_hangman = {
                "1" : " O ",
                "3" : "|",
                "5" : " | ",
                "4" : "\ ",
                "2" : "/",
                "7" : "\ ",
                "6" : "/",}

def display_hangman(number_of_incorrect_guesses, guess, word):
    if number_of_incorrect_guesses == 1:
        print("", parts_to_hangman["1"])
    elif number_of_incorrect_guesses == 2:
        print("", parts_to_hangman["1"],"\n", parts_to_hangman["2"])
    elif number_of_incorrect_guesses == 3:
        print("", parts_to_hangman["1"],"\n", parts_to_hangman["2"] + parts_to_hangman["3"])
    elif number_of_incorrect_guesses == 4:
        print("", parts_to_hangman["1"],"\n", parts_to_hangman["2"] + parts_to_hangman["3"] + parts_to_hangman["4"])
    elif number_of_incorrect_guesses == 5:
        print("", parts_to_hangman["1"],"\n", parts_to_hangman["2"] + parts_to_hangman["3"] + parts_to_hangman["4"],"\n", parts_to_hangman["5"])
    elif number_of_incorrect_guesses == 6:
        print("", parts_to_hangman["1"],"\n", parts_to_hangman["2"] + parts_to_hangman["3"] + parts_to_hangman["4"],"\n", parts_to_hangman["5"], "\n", parts_to_hangman["6"])
    elif number_of_incorrect_guesses == 7:
        print("", parts_to_hangman["1"],"\n", parts_to_hangman["2"] + parts_to_hangman["3"] + parts_to_hangman["4"],"\n", parts_to_hangman["5"], "\n", parts_to_hangman["6"], parts_to_hangman["7"])


def get_current_word(correct_guesses: list, hidden_word: str):
    current_word = ""
    for letter in hidden_word:
        current_word += letter if letter in correct_guesses else "_"
    return current_word


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

    max_incorrect_guesses = 7

    # Game loop is a while true loop
    while True:
        # Take input for hidden word and check if it is valid
        while True:
            hidden_word = input("Enter the hidden word: ")
            if all([letter in letter_dictionary for letter in hidden_word]):
                hidden_word = hidden_word.upper()
                break
            else:
                print("That is not a valid word. Try Again.")

        # for letter in hidden_word:
        #     if letter in letter_dictionary:
        #         new_hidden_word += letter_dictionary[letter]
        #         hidden_word = new_hidden_word




        # make the hidden word into the current word that will be displayed to the player
        number_of_letters = len(new_hidden_word)
        for i in range(number_of_letters):
            if i != " ":
                current_word += "_"
            else:
                current_word += " "


        # Take input for guesses and check if it is valid or if they want to exit or restart
        while True:
            guess = input("Enter a guess for the hidden word (or \"exit\" to exit): ")

            if guess == "exit":
                return            
            if len(guess) != 1:
                print("Guess not valid. Must be exactly one letter.")
                continue

            # we have a valid guess
            if guess in letter_dictionary:
                guess = letter_dictionary[guess]

            if guess in guesses:
                print("Already guessed. Try again.")
                continue

            guess_is_correct = check_guesses_letters(guess, hidden_word)

            if guess_is_correct:
                correct_guesses.append(guess)
            else:
                incorrect_guesses.append(guess)
                number_of_incorrect_guesses += 1

            print(get_current_word(correct_guesses, hidden_word))

            print(f"Your correct guesses are {correct_guesses}, and your incorrect guesses are {incorrect_guesses}")

            guesses.append(guess)
            print(f"Your guesses are {guesses}.")        

            display_hangman(number_of_incorrect_guesses, guess, hidden_word)



            if current_word == hidden_word:
                print("You Won the Game!")
                break
            if number_of_incorrect_guesses == 7:
                print("Game Over! You've been hanged!")
                break

            if not guess_is_correct:
                print(f"Incorrect! You have {max_incorrect_guesses - number_of_incorrect_guesses} guesses left.")

            # function returns invalid value. If it is a win, invalid = 1, if it is a loss invalid = 2, and if the game has to continue invalid = 0
            
hangman()