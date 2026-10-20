# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Chau
# Section: 571
# Assignment: Lab Topic 8
# Date: 20 October 2026

time = "1:11"
preferred_character = "*"

numbers_to_ascii = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

character_to_ascii = {
    "1": [" 1 ", "11 ", " 1 ", " 1 ", "111"],
    "A": [" A ", "A A", "AAA", "A A", "A A"],
    "M": ["M   M", "MM MM", "M M M", "M   M", "M   M"],
    ":": [" ", ":", " ", ":", " "]}

ascii_characters = []
for character in time:
    if character in character_to_ascii:
        ascii_character = character_to_ascii[character]
        if character in numbers_to_ascii:
            if preferred_character != "":
                for i in range(len(ascii_character)):
                    ascii_character[i] = ascii_character[i].replace(character, preferred_character)
        ascii_characters.append(ascii_character)

ascii_string = ""
for i in range(len(ascii_characters[0])):
    for ascii_character in ascii_characters:
        ascii_string += ascii_character[i] + " "
    ascii_string += "\n"

print(ascii_string)