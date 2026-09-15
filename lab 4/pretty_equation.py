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

from ast import If
from math import *

A=float(input("Please enter the coefficient A: "))
B=float(input("Please enter the coefficient B: "))
C=float(input("Please enter the coefficient C: "))

eq= "The quadratic equation is "
if A==0:
    eq += ""
elif A==1:
    eq += str("x^2 ")
elif A==-1:
    eq += str("- x^2 ")
elif A<0:
    eq += str(f"- {int(abs(A))}x^2 ")
elif A>1:
    eq += str(f"{int(A)}x^2 ")
if B==0:
    eq += str()
elif B==1 and A==0: #gets rid of the + sign if A is 0
    eq += str("x ")
elif B==1 and A!=0:
    eq += str("+ x ")
elif B==-1:
    eq += str("- x ")
elif B<0:
    eq += str(f"- {int(abs(B))}x ")
elif B>1 and A==0: #gets rid of the + sign if A is 0
    eq += str(f"{int(B)}x ")
elif B>1 and A!=0:
    eq += str(f"+ {int(B)}x ")
if C==0:
    eq += str()
elif C==1:
    eq += str("+ 1 ")
elif C<0:
    eq += str(f"- {int(abs(C))} ")
elif C>1:
    eq += str(f"+ {int(C)} ")
print(eq + "= 0")
