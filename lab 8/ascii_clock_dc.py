# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Chau
# Section: 571
# Assignment: Lab Topic 8
# Date: 20 October 2026

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