# Take user input for temperature
temperature = float(input("Enter the temperature in °C: "))

# Provide advice based on the temperature
if temperature > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temperature <= 30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")
