import math

x= float(input("enter the point x :"))
y= float(input("enter the point y :"))

# cordinates at center/
center_x=0
center_y=0
width=10
height=5

w=width/2
h=height/2

if  x <= w and  y <=h:
    print(f"The point ({x}, {y}) is inside the rectangle.")
else:
    print(f"The point ({x}, {y}) is outside the rectangle.")
