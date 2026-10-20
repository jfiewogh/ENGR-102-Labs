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

ascii = {
     "0" : "000\n0 0\n0 0\n0 0\n000",
     "1" : " 1 \n11 \n 1 \n 1 \n111", 
     "2" : "222\n  2\n222\n2  \n222", 
     "3" : "333\n  3\n333\n  3\n333", 
     "4" : "4 4\n4 4\n444\n  4\n  4", 
     "5" : "555\n5  \n555\n  5\n555", 
     "6" : "666\n6  \n666\n6 6\n666", 
     "7" : "777\n  7\n 77\n  7\n  7", 
     "8" : "888\n8 8\n888\n8 8\n888", 
     "9" : "999\n9 9\n999\n  9\n  9", 
     "A" : "A \nA A\nAAA\n A A\nA A",
     "P" : "PPP\nP P\nPPP\nP  \nP  ", 
     "M" : "M   M\nMM MM\nM M M\nM   M\nM   M",
     ":" : " \n:\n \n:\n "}

print(ascii[":"])


# Read input from the user
time_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ":"]
x = 0
time = input("Enter the time in a 24 hour format ")
time_parts = time.split(":")
hours, minutes = str(time_parts[0]), str(time_parts[1])
while x != 1:
    time_parts = time.split(":")
    hours, minutes = str(time_parts[0]), str(time_parts[1])

    for i in time:
        if i not in time_list:
            x = 0
        else:
            continue
    if not(int(hours) >= 0 and int(hours) < 24 and int(minutes) >= 0 and int(minutes) < 60):
        x = 0
    else:
        x = 1
    if x != 1:
        time = input("Error. Not a valid time. Try again ")
    else:
        break
clock_type = int(input("Enter the clock type. '24' for 24 hour format '12' for twelve hour format "))
preferred_character = input("Enter your preferred character to display the time ")
# Handle user input
if clock_type == 12:
    if int(hours) >= 13:
       time = str(int(hours) - 12) + ":" + str(minutes)
       time = str(time) + "PM"
    else: 
        if int(hours) >= 12:
            time = str(time) + "PM"
        elif int(hours) == 0:
            hours = int(hours) + 12
            time = f"{hours}:{minutes}" + "AM"

        else: 
            time = str(time) + "AM"
else:
    time = time

accetable_characters = ["a", "b", "c", "d", "e", "g", "h", "k", "m", "n", "p", "q", "r", "s", "u", "v", "w", "x", "y", "z", "@", "$", "&", "*", "="]
if not(preferred_character in accetable_characters or preferred_character == ''):
    print("Error. Character not valid.")
    input("Try again. Enter another preferred character ")



print(time)
print(preferred_character)

    



""" Display the time in ASCII art """

numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
character_to_ascii = {
    "1": [" 1 ", "11 ", " 1 ", " 1 ", "111"],
    "A": (" A ", "A A", "AAA", "A A", "A A"),
    "M": ("M   M", "MM MM", "M M M", "M   M", "M   M"),
    ":": (" ", ":", " ", ":", " ")}

time = "11:11AM"
preferred_character = "*"

# Initialize empty list with ASCII characters
ascii_characters = []
# Iterate through each character in time
for character in time:
    if character in character_to_ascii:
        # Get ASCII character
        ascii_character = character_to_ascii[character]
        # If character is a number and there is a preferred character, replace it with a preferred character
        if preferred_character != "" and character in numbers:
            for i in range(len(ascii_character)):
                ascii_character[i] = ascii_character[i].replace(character, preferred_character)
        # Add ASCII character to list of ASCII characters
        ascii_characters.append(ascii_character)

# Convert list of ASCII characters to a string
ascii_string = "\n".join([" ".join([ascii_character[i] for ascii_character in ascii_characters]) for i in range(len(ascii_characters[0]))])

# Output the ASCII string
print(ascii_string)