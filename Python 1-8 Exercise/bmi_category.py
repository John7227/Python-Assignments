weight = float(input("Enter Weight: "))

height = float(input("Enter Height: "))

bmi = weight / (height * height)


if bmi < 18.5:
	print("Underweight")
elif bmi >= 18.5 and bmi <= 19.9:
	print("Normal")
elif bmi >= 25 and bmi <= 29.9:
	print("Overweight")
elif bmi >= 30:
	print("Obese")