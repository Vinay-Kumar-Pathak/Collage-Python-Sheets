#  Decimal to hex

# The hex() function is used to convert the number into a hexadecimal string

num = int(input("Enter an integer between 0 and 15: "))
hex_value = hex(num)[2:].upper() 

if 0<=num<=15:
    print(" its hexvalue is :",hex_value)
else:
    print("invalid input ")    
