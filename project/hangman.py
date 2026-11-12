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
#Displaying hangman-leo
parts_to_hangman = {
        "1" : " O ",
        "3" : "|",
        "5" : " | ",
        "4" : "\ ",
        "2" : "/",
        "7" : "\ ",
        "6" : "/",}
number_of_incorrect_guesses = 0
list_incorrect_guesses = []
max_incorrect_guesses = 7

def display_hangman(number_of_incorrect_guesses, guess, word) :

    if guess not in word :
        number_of_incorrect_guesses += 1
        list_incorrect_guesses.append(guess)
        
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

def play_hangman():
    word = input("Enter a word for Hangman: ").lower() # learned what .lower() des
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 7

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print(display_word)

        if '_' not in display_word:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"Game over! The word was '{word}'.")



            

                
            
