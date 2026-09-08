from math import *
#y will be used to represent the distance in kilometers in the y direction at a given time
#x will be used to represent the distance in kilometers in the x direction at a given time
#z will be used to represent the distance in kilometers the z direction at a given time
#t will be used to represent any point in time in hours. 
#this code will perform a simple linear equation of a car traveling in a straight line at a constant rate of change 

ti=float(input("Enter time 1:"))
x1= float(input("Enter the x position of the object at time 1:"))
y1= float(input("Enter the y position of the object at time 1:"))
z1= float(input("Enter the z position of the object at time 1:"))
tf=float(input("Enter time 2:"))
xf= float(input("Enter the x position of the object at time 2:"))
yf= float(input("Enter the y position of the object at time 2:"))
zf= float(input("Enter the z position of the object at time 2:"))
t1= ti+((tf-ti)*.25)
t2= ti+((tf-ti)*.50)
t3=ti+((tf-ti)*.75)
#slope 
sx=(xf-x1)/(tf-ti)
sy=(yf-y1)/(tf-ti)
sz=(zf-z1)/(tf-ti)
eqx=sx*ti
eqy=sy*ti
eqz=sz*ti
print(f"At time {ti} second the obje t is at ({eqx},{eqy},{eqz})")
eqx=sx*t1
eqy=sy*t1
eqz=sz*t1
print(f"At time {t1} second the obje t is at ({eqx},{eqy},{eqz})")
eqx=sx*t2
eqy=sy*t2
eqz=sz*t2
print(f"At time {t2} second the obje t is at ({eqx},{eqy},{eqz})")
eqx=sx*t3
eqy=sy*t3
eqz=sz*t3
print(f"At time {t3} second the obje t is at ({eqx},{eqy},{eqz})")
eqx=sx*tf
eqy=sy*tf
eqz=sz*tf
print(f"At time {tf} second the obje t is at ({eqx},{eqy},{eqz})")
