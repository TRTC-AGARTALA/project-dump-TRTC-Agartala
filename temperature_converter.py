print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = input("Choose an option (1-4): ")
temperature = float(input("Enter temperature: "))

if choice == "1":
    result = (temperature * 9/5) + 32
    print("Temperature:", result, "°F")

elif choice == "2":
    result = (temperature - 32) * 5/9
    print("Temperature:", result, "°C")

elif choice == "3":
    result = temperature + 273.15
    print("Temperature:", result, "K")

elif choice == "4":
    result = temperature - 273.15
    print("Temperature:", result, "°C")

else:
    print("Invalid choice!")