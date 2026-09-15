# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 2
# Date: 15 September 2026
#
from ast import If
from math import *

############ Part A ############ 
a=input("Enter True or False for a: ")
b=input("Enter True or False for b: ")
c=input("Enter True or False for c: ")

A = a == 'True' or a == 'T' or a == 't'
B = b == 'True' or b == 'T' or b == 't'
C = c == 'True' or c == 'T' or c == 't'


############ Part B ############ 
d= (A) and (B) and (C)
e= (A) or (B) or (C)
print("a and b and c:", d)
print("a or b or c:", e)
############ Part C ############ 
XOR= (A) != (B)
print("XOR:", XOR)
od= (A) and not (B) and not (C) or not (A) and (B) and not (C) or not (A) and not (B) and (C) or (A) and (B) and (C)
print("Odd number:", od)
