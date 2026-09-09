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
#

from math import *
#y will be used to represent the distance in kilometers in the y direction at a given time
#x will be used to represent the distance in kilometers in the x direction at a given time
#z will be used to represent the distance in kilometers the z direction at a given time
#t will be used to represent any point in time in hours. 
#this code will perform a simple linear equation of a car traveling in a straight line at a constant rate of change 
ti=float(input("Enter time 1: "))
x1= float(input("Enter the x position of the object at time 1: "))
y1= float(input("Enter the y position of the object at time 1: "))
z1= float(input("Enter the z position of the object at time 1: "))
tf=float(input("Enter time 2: "))
xf= float(input("Enter the x position of the object at time 2: "))
yf= float(input("Enter the y position of the object at time 2: "))
zf= float(input("Enter the z position of the object at time 2: "))
print()
t1= ti+((tf-ti)*.25)
t2= ti+((tf-ti)*.50)
t3=ti+((tf-ti)*.75)
#slope 
sx=(xf-x1)/(tf-ti)
sy=(yf-y1)/(tf-ti)
sz=(zf-z1)/(tf-ti)
eqx=sx*(ti - ti) + x1
eqy=sy*(ti - ti) + y1
eqz=sz*(ti - ti) + z1
print(f"At time {ti:.2f} seconds the object is at ({eqx:.3f}, {eqy:.3f}, {eqz:.3f})")
eqx=sx*(t1 - ti) + x1
eqy=sy*(t1 - ti) + y1
eqz=sz*(t1 - ti) + z1
print(f"At time {t1:.2f} seconds the object is at ({eqx:.3f}, {eqy:.3f}, {eqz:.3f})")
eqx=sx*(t2- ti) + x1
eqy=sy*(t2- ti) + y1
eqz=sz*(t2- ti) + z1
print(f"At time {t2:.2f} seconds the object is at ({eqx:.3f}, {eqy:.3f}, {eqz:.3f})")
eqx=sx*(t3- ti) + x1
eqy=sy*(t3- ti) + y1
eqz=sz*(t3- ti) + z1
print(f"At time {t3:.2f} seconds the object is at ({eqx:.3f}, {eqy:.3f}, {eqz:.3f})")
eqx=sx*(tf- ti) + x1
eqy=sy*(tf- ti) + y1
eqz=sz*(tf- ti) + z1
print(f"At time {tf:.2f} seconds the object is at ({eqx:.3f}, {eqy:.3f}, {eqz:.3f})")
