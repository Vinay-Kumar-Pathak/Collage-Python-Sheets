# Problem 2: (Find future dates)
a=int(input("Enter today's day:"))
b=int(input("Enter the number of days elapsed since today:"))

days_in_week=["sunday","monday","tuesday","wednesday","thrusday","friday","saturday"]

# Calculate the future day of the week
future_day = (a + b) % 7



# Output the future day of the week
print(f"In {days_in_week[a]} days, future day will be {days_in_week[future_day]}.")