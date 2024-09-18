# Science: calculate energy

#weight of water
m = float(input("weight of water in kilogram : "))



#initial temperature
initialtemperature =float(input("inter the initial temperature in degrees Celsius : "))

#final temperature
finaltemperature =float(input("inter the final temperature in degrees Celsius : "))


# formula

q= m * (finaltemperature-initialtemperature) * 4184

print(q,("joules"))