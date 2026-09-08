from math import *
#py will be used to represent the distance in kilometers in the y direction at a given time
#px will be used to represent the distance in kilometers in the x direction at a given time
#pz will be used to represent the distance in kilometers the z direction at a given time
#t will be used to represent any point in time in hours. 
#this code will perform a simple linear equation of a car traveling in a straight line at a constant rate of change 

t=float(input("Eneter time 1:"))
print(t)
px=1*t
py=1*t
pz=1*t
print("At time 1.00 seconds the object is at(",px,",",py,",",pz,")")
x= (input("Enter the x position of the object at time 1:"))
y= (input("Enter the y position of the object at time 1:"))
z= (input("Enter the  position of the object at time 1:"))
Tx= px/1
Ty= py/1
Tz= pz/1
