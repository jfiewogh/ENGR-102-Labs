# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 11 Part 2
# Date: 12 November 2026

# Get infile name from user
valid_passports = []
infile_name = input("Enter the name of the file: ")

# Get passports from infile
with open(infile_name, "r") as infile:
    passports = infile.read().split("\n\n")

def get_element_value(element: str) -> str:
    """ Returns part of string after the colon """
    return element[element.index(":") + 1:]

valid_passports = []

# Loop through each passport string
for passport in passports:
    # Initialize valid_passport_elements as 0
    valid_passport_elements = 0
    # Loop through each element of passport
    for element in passport.split():
        element_value = get_element_value(element)

        if "byr" in element:
            # Birth year must be between 1922 and 2010, inclusive
            if int(element_value) >= 1922 and int(element_value) <= 2010:
                valid_passport_elements += 1
        elif "iyr" in element:
            # Issue year must be between 2016 and 2026, inclusive
            if int(element_value) >= 2016 and int(element_value) <= 2026: 
                valid_passport_elements += 1
        elif "eyr" in element:
            # Expiration year must between 2026 and 2036, inclusive
            if int(element_value) >= 2026 and int(element_value) <= 2036:
                valid_passport_elements += 1
        elif "hgt" in element:
            # Height must be a number followed by either cm or in
            if element_value[-2:] == "in":
                number = int(element_value[:-2])
                # If in, number must be between 59 and 76, inclusive
                if number >= 59 and number <= 76:
                    valid_passport_elements += 1
            elif element_value[-2:] == "cm":
                number = int(element_value[:-2])
                # If cm, number must be between 150 and 193, inclusive
                if number >= 150 and number <= 193:
                    valid_passport_elements += 1
        elif "hcl" in element: 
            # Hair color must be # followed by exactly 6 characters (0-9 or a-f)
            if element_value[0] == "#":
                num_chars = 0
                for char in element_value[1:]: 
                    if char in "0123456789abcdef":
                        num_chars += 1
                if num_chars == 6:
                    valid_passport_elements += 1
        elif "ecl" in element:
            # Eye color must be one of the following: amb, blu, brn, gry, grn, hzl, oth
            if element_value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                valid_passport_elements += 1
        elif "cid" in element:
            # Get first index of character that is not 0
            for i in range(0, len(element_value)):
                if element_value[i] != "0":
                    break
            id = element_value[i:]
            if len(id) == 3:
                valid_passport_elements += 1

    # Passport is valid if seven elements are valid
    if valid_passport_elements == 7:
        valid_passports.append(passport)

# Write valid passports to outfile
with open("valid_passports2.txt", "w") as outfile:
    outfile.write("\n\n".join(valid_passports))

# Output number of valid passports
print(f"There are {len(valid_passports)} valid passports")