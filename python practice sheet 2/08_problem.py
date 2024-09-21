charecter = input("Enter a hex character (0-9, A-F): ")

decimal_value = int(charecter, 16)  

if charecter in '0123456789ABCDEF':
     print(f"The decimal value of hex character '{charecter}' is {decimal_value}.")
else:
     print("Invalid input! Please enter a valid hex character (0-9 or A-F).")
