import math

x= float(input("enter the point x :"))
y= float(input("enter the point y :"))

# cordinates at center/
# center_x=0
# center_y=0
# pointx=(200,0)
# pointy=(100,0)

# if :
#     print(f"point of x and y is inside the triangle {x},{y}")
# else:
#     print("not in triangle")


def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

# area of origianl triangle
original=triangle_area(0,0,200,0,0,100)
print(original)
A
# area of other remaining triangles
area1= triangle_area(x,y,200,0,0,100)
area2= triangle_area(0,0,x,y,0,100)
area3= triangle_area(0,0,200,0,x,y)

# check the point is in the triangele

if(original == (area1 + area2 + area3)):
    print("Point is in the triangel...")
else:
    print("Point is not in the triangel...")

