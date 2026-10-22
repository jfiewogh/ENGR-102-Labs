# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 8
# Date: 20 October 2026

""" Initialize dictionary """

# Initialize dictionary mapping character to ascii string representing character
character_to_ascii = {
    "0" : "000\n0 0\n0 0\n0 0\n000",
    "1" : " 1 \n11 \n 1 \n 1 \n111", 
    "2" : "222\n  2\n222\n2  \n222", 
    "3" : "333\n  3\n333\n  3\n333", 
    "4" : "4 4\n4 4\n444\n  4\n  4", 
    "5" : "555\n5  \n555\n  5\n555", 
    "6" : "666\n6  \n666\n6 6\n666", 
    "7" : "777\n  7\n  7\n  7\n  7", 
    "8" : "888\n8 8\n888\n8 8\n888", 
    "9" : "999\n9 9\n999\n  9\n999", 
    "A" : " A \nA A\nAAA\nA A\nA A",
    "P" : "PPP\nP P\nPPP\nP  \nP  ", 
    "M" : "M   M\nMM MM\nM M M\nM   M\nM   M",
    ":" : " \n:\n \n:\n "}

""" Read input from the user """

# Get time
time = input("Enter the time: ")
while True:
    # Check if character is permitted
    character_permitted = True
    for character in time:
        if character not in "1234567890:":
            character_permitted = False
            break
    if not character_permitted:
        # If character not permitted, prompt user to try again and go to next iteration
        time = input("Character not permitted! Try again: ")
        continue
    
    # Check if there is hours and minutes
    time_parts = time.split(":")
    if len(time_parts) != 2:
        # If not a valid time, prompt user to try again and go to next iteration
        time = input("Not a valid time! Try again: ")
        continue
    
    # Check if hours in 0 to 23 and minutes in 0 to 59
    hours, minutes = int(time_parts[0]), int(time_parts[1])
    if not (hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59):
        # If not a valid time, prompt user to try again and go to next iteration
        time = input("Not a valid time! Try again: ")
        continue

    # Exit out of loop if valid time
    break

# Get clock type
clock_type = input("Choose the clock type (12 or 24): ")
while not (clock_type == "12" or clock_type == "24"):
    clock_type = input("Clock type must be 12 or 24. Try again: ")

# Get preferred character
preferred_character = input("Enter your preferred character: ")
while preferred_character not in "abcdeghkmnopqrsuvwxyz@$&*=":
    preferred_character = input("Character not permitted! Try again: ")

# Modify time based on clock type
if clock_type == "12":
    # Get meridian
    if hours >= 13:
        meridiem = "PM"
    else:
        meridiem = "AM"
    # Get hours
    hours %= 12
    if hours == 0:
        hours = 12
    # Set to new time
    time = f"{hours}:{minutes:0>2}{meridiem}"

""" Display the time in ASCII art """

# Initialize empty list with ASCII characters
ascii_characters = []
# Iterate through each character in time
for character in time:
    if character in character_to_ascii:
        # Get ASCII character
        ascii_character = character_to_ascii[character]
        # If character is a number and there is a preferred character, replace it with a preferred character
        if preferred_character != "" and character in "1234567890":
            for i in range(len(ascii_character)):
                ascii_character = ascii_character.replace(character, preferred_character)
        # Add ASCII character to list of ASCII characters
        ascii_characters.append(ascii_character)

# Convert list of ASCII characters to a string
ascii_string = "\n".join([" ".join([ascii_character.split("\n")[i] for ascii_character in ascii_characters]) for i in range(len(ascii_characters[0].split("\n")))])

# Output the ASCII string
print("\n" + ascii_string)