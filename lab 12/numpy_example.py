# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 12
# Date: 19 November 2026

# As a team, we have gone through all required sections of the 
# tutorial, and each team member understands the material

import numpy as np

# ii
A = np.arange(12).reshape(3, 4)
print(f"A = {A}")
print()

B = np.arange(8).reshape(4, 2)
print(f"B = {B}")
print()

C = np.arange(6).reshape(2, 3)
print(f"C = {C}")
print()

# iii
D = A @ B @ C
print(f"D = {D}")
print()

# iv
print(f"D^T = {np.transpose(D)}")
print()

# v
E = np.sqrt(D) / 2
print(f"E = {E}")