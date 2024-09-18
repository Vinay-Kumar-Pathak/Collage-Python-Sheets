#Health applicaOon: compute BMI)

POUNDS_TO_KG = 0.45359237
INCHES_TO_METERS = 0.0254

height1=float(input("enter a height in inches : "))

weight1=float(input("enter a weight in pounds : "))

# Convert weight to kilograms and height to meters
weight= weight1 * POUNDS_TO_KG
height = height1 * INCHES_TO_METERS


# formula
#BMI=float((weight*0.45359237)/((height*height)*0.0254))
bmi = weight/ (height ** 2)

print(bmi)