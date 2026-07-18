first_number = int(input("Enter First Number: "))

second_number = int(input("Enter Second Number: "))


if first_number > 0 and second_number > 0:
	print("Q1")
elif first_number < 0 and second_number > 0:
	print("Q2")
elif first_number < 0 and second_number < 0:
	print("Q3")
elif first_number > 0 and second_number < 0:
	print("Origin")
elif second_number == 0 and first_number != 0:
	print("X-axis")
elif first_number == 0 and second_number != 0:
	print("Y-axis")
else:
	print("Invalid number!")