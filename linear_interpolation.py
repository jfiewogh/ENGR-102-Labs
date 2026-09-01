# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:    David Chau
#           Zymraan
#           Leo
# Section: 571
# Assignment: Lab 2
# Date: 1 September 2026
#

"""
y = (slope)(x - x1) + y1

slope = (y2 - y1) / (x2 - x1)

y(x) = ((y2 - y1) / (x2 - x1)) * (x - x1) + y1

(10, 2030) = (x1, y1)
(55, 23030) = (x2, y2)

"""

# Part 1
print("Part 1:")

slope= (23030-2030)/45
y1=2030
x1=10

"""
Part 1:
For t = 25 minutes, the position p = 9030.0 kilometers
Part 2:
For t = 300 minutes, the position p = 10223.078642554414 kilometers
"""

t = 25
f=slope*(t-x1)+y1
print("For t =", t, "minutes, the position p =", f, "kilometers")





# Part 2
print("Part 2:")


