def celsius_to_fahrenheit(celsius):
    fahrenheit =(celsius * 9 /5 )+32
    return fahrenheit
c=float(input("enter temperature in celsius:"))
f= celsius_to_fahrenheit(c)

print("Temperature in fahrenheit:",f)