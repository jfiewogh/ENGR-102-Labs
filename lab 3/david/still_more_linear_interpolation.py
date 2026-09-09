# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 3
# Date: 8 September 2026

from math import *

# This code will perform a simple linear equation of a car traveling in a straight line at a constant rate of change 
# y will be used to represent the distance in kilometers in the y direction at a given time
# x will be used to represent the distance in kilometers in the x direction at a given time
# z will be used to represent the distance in kilometers the z direction at a given time
# t will be used to represent any point in time in hours. 

# Prompt the user for time 1 and the x, y, z positions at time 1
t_0 = float(input("Enter time 1: "))
x_0 = float(input("Enter the x position of the object at time 1: "))
y_0 = float(input("Enter the y position of the object at time 1: "))
z_0 = float(input("Enter the z position of the object at time 1: "))

# Prompt the user for time 2 and the x, y, z positions at time 2
t_f = float(input("Enter time 2: "))
x_f = float(input("Enter the x position of the object at time 2: "))
y_f = float(input("Enter the y position of the object at time 2: "))
z_f = float(input("Enter the z position of the object at time 2: "))

print()

# Calculate and store the three intermediate times in t_1, t_2, and t_3
t_1 = t_0 + ((t_f - t_0) * 0.25)
t_2 = t_0 + ((t_f - t_0) * 0.50)
t_3 = t_0 + ((t_f - t_0) * 0.75)

# Calculate the x, y, z slopes and store in m_x, m_y, and m_z
m_x = (x_f - x_0) / (t_f - t_0)
m_y = (y_f - y_0) / (t_f - t_0)
m_z = (z_f - z_0) / (t_f - t_0)

# Print position at time t_0
print(f"At time {t_0:.2f} seconds the object is at ({x_0:.3f}, {y_0:.3f}, {z_0:.3f})")

# Use linear interpolation to estimate and print position at time t_1
x_1 = m_x * (t_1 - t_0) + x_0
y_1 = m_y * (t_1 - t_0) + y_0
z_1 = m_z * (t_1 - t_0) + z_0
print(f"At time {t_1:.2f} seconds the object is at ({x_1:.3f}, {y_1:.3f}, {z_1:.3f})")

# Use linear interpolation to estimate and print position at time t_2
x_2 = m_x * (t_2 - t_0) + x_0
y_2 = m_y * (t_2 - t_0) + y_0
z_2 = m_z * (t_2 - t_0) + z_0
print(f"At time {t_2:.2f} seconds the object is at ({x_2:.3f}, {y_2:.3f}, {z_2:.3f})")

# Use linear interpolation to estimate and print position at time t_3
x_3 = m_x * (t_3 - t_0) + x_0
y_3 = m_y * (t_3 - t_0) + y_0
z_3 = m_z * (t_3 - t_0) + z_0
print(f"At time {t_3:.2f} seconds the object is at ({x_3:.3f}, {y_3:.3f}, {z_3:.3f})")

# Print position at time t_f
print(f"At time {t_f:.2f} seconds the object is at ({x_f:.3f}, {y_f:.3f}, {z_f:.3f})")