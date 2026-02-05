PROGRAM TO FIND TEMPATURE CONVERSION
1RUA25BCA0006
ADITI.M

temp = float(input("Enter temperature: "))
unit = input("Enter unit (C or F): ")

if unit == "C":
    print("Temperature in Fahrenheit:", (temp * 9/5) + 32)
elif unit == "F":
    print("Temperature in Celsius:", (temp - 32) * 5/9)
else:
    print("Invalid unit")
