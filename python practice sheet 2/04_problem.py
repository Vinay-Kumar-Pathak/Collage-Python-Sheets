# Problem 4: (Geometry: point in a circle?)
import math

x= float(input("enter the point x :"))
y= float(input("enter the point y :"))

# cordinates at center/
center_x=0
center_y=0

radius=10

distance= float(math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2))

if distance <= radius:
    print(f"The point ({x}, {y}) is inside the circle.")
else:
    print(f"The point ({x}, {y}) is outside the circle.")



