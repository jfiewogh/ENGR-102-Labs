# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 6
# Date: 24 September 2026
#
from ast import If
from math import *
# Code needs to measure the levels of totals cubes, then needs to measure the surface area of the pyrqamid 
# To get total number of cubes we need to perform a series of sums from the input value to one, and each layer is a (X)^2 
L = float(input("Enter the side length in meters: "))
n = int(float(input("Enter the number of layers: ")))
a=0
for i in range (1, n+1):
    a += ((i*L)**2) + (4*(i*L)*L)- (((i-1)*L)**2) # caluclates the SA of the bottom section minues the area where they join
print(f"You need {a:.2f} m^2 of gold foil to cover the pyramid")
