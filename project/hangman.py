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
    
        

            

                
            
