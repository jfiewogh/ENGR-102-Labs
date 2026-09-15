# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 1
# Date: 1 September 2026
#
from ast import If
from math import *

A=float(input("Please enter the coefficient A: "))
B=float(input("Please enter the coefficient B: "))
C=float(input("Please enter the coefficient C: "))
print()
if A==0:
    a=str()
elif A==1:
    a=str("x^2")
elif A==-1:
    a=str("- x^2")
elif A<0:
    a=str(f"- {int(abs(A))}x^2")
elif A>1:
    a=str(f"{int(A)}x^2")
if B==0:
    b=str()
elif B==1:
    b=str("+ x")
elif B==-1:
    b=str("- x")
elif B<0:
    b=str(f"- {int(abs(B))}x")
elif B>1:
    b=str(f"+ {int(B)}x")
if C==0:
    c=str()
elif C==1:
    c=str("+ 1")
elif C<0:
    c=str(f"- {int(abs(C))}")
elif C>1:
    c=str(f"+ {int(C)}")
print(f"The quadratic equation is {a} {b} {c} = 0")
