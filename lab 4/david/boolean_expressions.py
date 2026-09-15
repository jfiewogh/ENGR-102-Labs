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

############ Part A ############ 

# Prompt the user for a, b, and c
a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")

# Convert a, b, and c into booleans
A = a == 'True' or a == 'T' or a == 't'
B = b == 'True' or b == 'T' or b == 't'
C = c == 'True' or c == 'T' or c == 't'

############ Part B ############ 
print(f"a and b and c: {A and B and C}")
print(f"a or b or c: {A or B or C}")

############ Part C ############ 
print(f"XOR: {A and not B or not A and B}")
print(f"Odd number: {A and not B and not C or not A and B and not C or not A and not B and C or A and B and C}")

############ Part D ############ 
"""
(not (A and not B) or (not C and B)) and (not B) or (not A and B and not C) or (A and not B)}
(not A or B or not C and B) and not B or (not A and B and not C) or (A and not B)
(not A or B) and not B or (not A and B and not C) or (A and not B)
(not A and not B or B and not B) or (not A and B and not C) or (A and not B)
(not A and not B) or (not A and B and not C) or (A and not B)
not B and (not A or A) or (not A and B and not C)
not B or (not A and B and not C)
not B or (not A and not C)
"""
print(f"Complex 1: {(not (A and not B) or (not C and B)) and (not B) or (not A and B and not C) or (A and not B)}")
print(f"Simple 1: {not B or (not A and not C)}")

"""
(not ((B or not C) and (not A or not C))) or (not (C or not (B and C))) or (A and not C) and (not A or (A and B and C) or (A and ((B and not C) or (not B))))
(not (B or not C) or not (not (A and C)) or (not C and B and C) or (A and not C) and ((not A and A or not A and B or not A and C) or (A and (not B or not C))
(not B and C or A and C) or (A and not C) and ((not A and B or not A and C) or (A and not B or A and not C))
(not B and C or A and C) or (A and not C) and (not A and (B or C) or A and (not B or not C))
(not B and C or A and C) or (A and not C and not A and (B or C)) or (A and not C and A and (not B or not C))
(not B and C or A and C) or (A and not C and (not B or not C))
(not B and C) or (A and C) or (A and not C)
(not B and C) or A and (C or not C)
(not B and C) or A
"""
print(f"Complex 2: {(not ((B or not C) and (not A or not C))) or (not (C or not (B and C))) or (A and not C) and (not A or (A and B and C) or (A and ((B and not C) or (not B))))}")
print(f"Simple 2: {(not B and C) or A}")