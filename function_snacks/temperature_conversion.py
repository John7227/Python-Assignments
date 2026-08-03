def temperature_fahrenheit(value, symbol):

	val = float(value)
	if symbol == "C" or symbol == "c":
		celsius = val
		# celsius = float(input("Enter Celsius: "))
		fahrenheit = celsius * 9/5 + 32
	elif symbol == "F" or symbol == "f":
		fahrenheit = val
		# fahrenheit = float(input("Enter fahrenheit: "))
		celsius = fahrenheit - 32 * 5/9
	else:
		return "Invalid Input"

	threshold = 50

	if celsius < threshold or fahrenheit < threshold:
		return "Cold advisory"
	else:
		return "Heat alert"


value = input("Enter Value: ")
symbol = input("Enter Temperature Value(C / F): ")

print(temperature_fahrenheit(value, symbol))

