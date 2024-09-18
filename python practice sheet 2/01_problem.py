# Problem 1: (Algebra: solve linear equa2ons)
# You can use Cramer’s rule 

# input the values
a=float(input("enter the value a :"))
b=float(input("enter the value b :"))
c=float(input("enter the value c :"))
d=float(input("enter the value d :"))
e=float(input("enter the value e :"))
f=float(input("enter the value f :"))

# formula
x=((e*d)-(b*f))/((a*d)-(b*c))

y=((a*f)-(e*c))/((a*d)-(b*c))

if ((a*d)-(b*c))==0:
    print("the equation has no solution")
else:
    print("value of x is :",x,  "value of y is :",y)    