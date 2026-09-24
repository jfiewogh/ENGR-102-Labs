# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab Topic 6
# Date: 24 September 2026

# Prompt the user for side length and number of layers
side_length = float(input("Enter the side length in meters: "))
num_layers = int(input("Enter the number of layers: "))

# Calculate area of one face of cube
square = side_length ** 2

# Iterate through each layer of pyramid from 1 to num_layers, inclusive
# Then, add surface area to sum
sum = 0
for i in range(1, num_layers + 1):
    # Solve for the side surface area
    side = square * i * 4
    # Solve for the top surface area
    top = square * (i ** 2 - (i - 1) ** 2)
    # Add both to sum
    sum += side + top

# Output the calculated sum
print(f"You need {sum:.2f} m^2 of gold foil to cover the pyramid")