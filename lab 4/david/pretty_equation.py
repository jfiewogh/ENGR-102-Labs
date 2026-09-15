# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 4
# Date: 15 September 2026

from math import *

# Prompt the user for the coefficients A, B, and C
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

expression = ""

# Modify expression based on value and sign of A
if A != 0:
    if A < 0:
        expression += "- "
    if abs(A) > 1:
        expression += str(abs(A))
    expression += "x^2 "

# Modify expression based on value and sign of B
if B != 0:
    if B < 0:
        expression += "- "
    elif A != 0:
        expression += "+ "
    if abs(B) > 1:
        expression += str(abs(B))
    expression += "x "

# Modify expression based on value and sign of C
if C != 0:
    if C < 0:
        expression += "- "
    else:
        expression += "+ "
    expression += f"{abs(C)} "

# Print the quadratic equation
print(f"The quadratic equation is {expression}= 0")