# scissor, paper, rock
import random as rd


# take random variables inrange 0-2
b=rd.randint(0,2)
# print(b)


# taking the value form the user
a=int(input("scissor (0), rock (1), paper (2): "))

# the fix names
arr={
    0:"scissor",
    1:"rock",
    2:"paper"
}
# logic to give the right answers
if(a==b):
    print(f"The computer is {arr[b]}. You are {arr[a]}. You won.")
else:
    print(f"The computer is {arr[b]}. You are {arr[a]}. You lost.")
