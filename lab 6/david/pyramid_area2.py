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

# Calculate the first term and last term of the arithmetic series
first_term = square * 5
last_term = first_term + (num_layers - 1) * (square * 6)
# Use arithmetic sum formula to calculate sum of the series
sum = num_layers / 2 * (first_term + last_term)

# Output the calculated sum
print(f"You need {sum:.2f} m^2 of gold foil to cover the pyramid")