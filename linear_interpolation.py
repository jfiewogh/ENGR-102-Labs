# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan Khan
#           Leonardo Valle Gomez
# Section: 571
# Assignment: Lab 2
# Date: 1 September 2026
#

from math import *

"""
Part 1:
For t = 25 minutes, the position p = 9030.0 kilometers

y = (slope)(x - x1) + y1
slope = (y2 - y1) / (x2 - x1)
y = (y2 - y1) / (x2 - x1) * (x - x1) + y1
"""

print("Part 1:")

# time t1 = 10 minutes
t1 = 10
# position p1 = 2030 kilometers
p1 = 2030

# time t2 = 55 minutes
t2 = 55
# position p2 = 23030 kilometers
p2 = 23030

slope = (p2 - p1) / (t2 - t1)

# time t = 25 minutes
t = 25
# Use linear interpolation to estimate position p at t = 25 minutes
p = slope * (t - t1) + p1

print("For t =", t, "minutes, the position p =", p, "kilometers")


"""
Part 2:
For t = 300 minutes, the position p = 10223.078642554414 kilometers
"""

print("Part 2:")

radius = 6745

# circumference of circle = 2 * pi * radius
circumference = 2 * pi * radius

t = 300

p = slope * (t - t1) + pi

print(p)