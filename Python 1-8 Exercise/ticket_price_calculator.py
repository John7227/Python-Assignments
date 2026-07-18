age = int(input("Enter Age: "))

if age < 5:
	print("Free")
elif age >= 5 and age <= 12:
	print("$5")
elif age >= 13 and age < 65:
	print("$12")
elif age >= 65:
	print("$8")