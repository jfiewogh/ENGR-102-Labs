# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 9
# Date: 27 October 2026

def print_puzzle(puzzle: str) -> None:
    """ Print puzzle as a long division problem. """
    puzzle = puzzle.split(",")
    for i in range(len(puzzle)):
        if i == 1:
            print(f"{len(puzzle[i].split('|')[1]) * '_': >16}")
        print(f"{puzzle[i]: >16}")
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def get_valid_letters(puzzle: str) -> str:
    """ Return one string of ten unique letters in the puzzle string """
    # Initialize valid_letters as empty list
    valid_letters = []
    # Iterate through each character of the puzzle string
    for char in puzzle:
        # Add to valid_letters list if character is a letter and not already in list
        if char not in valid_letters and char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            valid_letters.append(char)
    # Convert list to string
    return "".join(valid_letters)

def is_valid_guess(valid_letters, user_guess) -> bool:
    count = 0
    for letter in user_guess:
        if letter in valid_letters:
            count += 1
    return count == 10

def check_user_guess(dividend: int, quotient: int, divisor: int, remainder: int) -> bool: 
    if dividend == quotient * divisor + remainder: 
        return True 
    else : 
        return False

        
def make_number(word: str, guess: str) -> int:
    guess_list = list(guess)
    dictionary_of_values_of_letters = {}
    n = 0
    for i in guess:
        dictionary_of_values_of_letters[i] = n
        n += 1

    concatenation = ""
    for i in word:
        concatenation += str(dictionary_of_values_of_letters[i])
    number = int(concatenation)
    return number

def make_numbers(puzzle: str, guess: str) -> tuple[int]:
    """ Returns tuple of four values that are the equivalent integers of the words representing the dividend, quotient, divisor, and remainder """
    # Parse the puzzle string for the words representing the dividend, quotient, divisor, and remainder
    left, right = puzzle.split("|")
    left_parts = left.split(",")
    quotient = left_parts[0].strip()
    divisor = left_parts[1].strip()
    right_parts = right.split(",")
    dividend = right_parts[0].strip()
    remainder = right_parts[-1].strip()
    # Convert each word to number and return
    return make_number(dividend, guess), make_number(quotient, guess), make_number(divisor, guess), make_number(remainder, guess)

def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    puzzle = "RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"

    # testing
    valid_letters = get_valid_letters(puzzle)
    print(valid_letters)

    

    print(make_numbers(puzzle, "TAKEOURSIM"))



    print()
    print_puzzle(puzzle)

if __name__ == "__main__":
    main()

print(make_number("RUE", "TAKEOURSIM"))