#Geometry: area of a triangle



#enter the points
x1=float(input("enter the value of first x1 :"))
y1=float(input("enter the value of first y1 :"))
x2=float(input("enter the value of first x2 :"))
y2=float(input("enter the value of first y2 :"))
x3=float(input("enter the value of first x3 :"))
y3=float(input("enter the value of first y3 :"))

# formula
side1=((x2-x1)**2 +(y2-y1)**2)**(1/2)
side2=((x3-x2)**2 +(y3-y2)**2)**(1/2)
side3=((x1-x3)**2 +(y1-y3)**2)**(1/2)
s=(side1+side2+side3)/2
area=((s*(s-side1)*(s-side2))*(s-side3))**(1/2)

print(("area of a triangle"),area)