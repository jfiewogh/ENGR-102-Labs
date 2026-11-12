# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 11
# Date: 12 November 2026

# Get infile name
infile_name = input("Enter the name of the file: ")

# Get passports from infile
with open(infile_name, "r") as infile:
    passports = infile.read().split("\n\n")

def is_valid(passport: str) -> bool:
    """ Return whether the passport is valid """
    return "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "cid" in passport

# Initialize valid_passports as empty list
valid_passports = []
for passport in passports:
    if is_valid(passport):
        # Add passport to list if contains all required components
        valid_passports.append(passport)

# Open valid_passports.txt as outfile
with open("valid_passports.txt", "w") as outfile:
    # Write passports to outfile
    outfile.write("\n\n".join(valid_passports))

# Output number of valid passports
print(f"There are {len(valid_passports)} valid passports")