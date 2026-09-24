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

import math

# Continuously get value for x until in within range (0, 2]
x = float(input("Enter a value for x: "))
while not 0 < x <= 2:
    x = float(input("Out of range! Try again: "))

# Get the tolerance from the user
tolerance = float(input("Enter the tolerance: "))

sum = 0.0
n = 1
while True:
    # Calculate the nth term
    term = (-1) ** (n - 1) * (x - 1) ** n / n
    # Exit out of loop if magnitude of term is less than tolerance
    if abs(term) < tolerance:
        break
    # Add term to sum
    sum += term
    # Increment n by 1
    n += 1

# Output the approximate value, exact value, and magnitude of difference
print(f"ln({x}) is approximately {sum}")
exact = math.log(x)
print(f"ln({x}) is exactly {exact}")
print(f"The difference is {abs(sum - exact)}")