charecter=input(" enter a hex character :").upper

if charecter in '0123456789ABCDEF':
     decimal_value = int(charecter, 16)
     print(f"The decimal value of hex character '{charecter}' is {decimal_value}.")
else:
     print("Invalid input! Please enter a valid hex character (0-9 or A-F).")
