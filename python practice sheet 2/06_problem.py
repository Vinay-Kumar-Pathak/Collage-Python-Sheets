def triangle_area(x1, y1, x2, y2, x3, y3):
    # Calculate the lengths of the sides
    side1 = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    side2 = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
    side3 = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
    s = (side1 + side2 + side3) / 2
    area = (s * (s - side1) * (s - side2) * (s - side3))**0.5
    return area

x= float(input("enter the point x :"))
y= float(input("enter the point y :"))


# area of origianl triangle
original=triangle_area(0,0,200,0,0,100)

#  area of other remaining triangles
area1= triangle_area(x,y,200,0,0,100)
area2= triangle_area(0,0,x,y,0,100)
area3= triangle_area(0,0,200,0,x,y)

# check the point is in the triangele

if(original >= (area1 + area2 + area3)):
    print("Point is in the triangle")
else:
    print("Point is not in the triangle")

