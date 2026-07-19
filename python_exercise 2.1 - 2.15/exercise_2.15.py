first_number = float(input("Enter First Number: "))
second_number = float(input("Enter Second Number: "))
third_number = float(input("Enter Third Number: "))

if first_number > second_number:
	first_number, second_number = second_number, first_number
elif second_number > third_number:
	second_number, third_number = third_number, second_number
elif first_number > second_number:
	first_number, second_number = second_number, first_number

print(first_number)
print(second_number)
print(third_number)