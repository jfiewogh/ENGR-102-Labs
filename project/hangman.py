from math import *
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



            

                
            
