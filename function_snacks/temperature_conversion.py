def temperature_fahrenheit(fahrenheit):

	celsius = fahrenheit - 32 * 5/9
	fahrenheit = celsius * 9/5 + 32

	threshold = 50


	if celsius < threshold:
		return "Cold advisory"
	elif celsius >= threshold:
		return "Heat alert"

	if fahrenheit < threshold:
		return "Cold advisory"
	elif fahrenheit >= threshold:
		return "Heat alert"


celsius = float(input("Enter Celsius: "))
fahrenheit = float(input("Enter fahrenheit: "))

print(temperature_fahrenheit(celsius))
print(temperature_fahrenheit(fahrenheit))

