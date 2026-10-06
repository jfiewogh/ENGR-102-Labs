
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 5
# Date: 01 October 2026
# 
import math
from math import log
x = float(input("Enter a value for x: "))
while x <= 0 or x > 2:
    x = float(input("Out of range! Try again: "))
tol = float(input("Enter the tolerance: "))
# exact value of ln(x)
lnx = log(x)
# approximate value of ln(x) using Taylor series expansion
Alnx = (x - 1)
i = 2
z = -1
term = (z * (x - 1)**i) / i
while abs(term) >= tol:
    term = (z * (x - 1)**i) / i
    Alnx = Alnx + term
    i += 1
    z *= -1
    term = (z * (x - 1)**i) / i
print("ln(", x, ") is approximately ", Alnx, sep="")
print("ln(", x, ") is exactly ", lnx, sep="")
print("The difference is ", abs(lnx - Alnx), sep="")