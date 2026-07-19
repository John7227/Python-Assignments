age = int(input("Enter Age: "))

if age >= 20:
	print("Adult")
elif age >= 13 and age <= 20:
	print("Teen")
elif age >= 0 and age <= 12:
	print("Child")
else:
	print("Invalid input")