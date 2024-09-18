#Geometry: area of a triangle

import math

#enter the points
x1=float(input("enter the value of first x1 :"))
y1=float(input("enter the value of first y1 :"))
x2=float(input("enter the value of first x2 :"))
y2=float(input("enter the value of first y2 :"))
x3=float(input("enter the value of first x3 :"))
y3=float(input("enter the value of first y3 :"))

# formula
side1= x1*(y2-y3)
side2= x2*(y3-y1)
side3= x3*(y1-y2)
s=abs((side1+side2+side3)/2)



print(("area of a triangle"),s)