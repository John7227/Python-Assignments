first_number = int(input("Enter First Number: "))

second_number = int(input("Enter Second Number: "))

third_number = int(input("Enter Third Number: "))

sum = first_number + second_number + third_number
average = sum / 3
product = first_number * second_number * third_number

smallest = first_number

if second_number < smallest and second_number < third_number:
	smallest = second_number
elif third_number < second_number and third_number < second_number and third_number < first_number and third_number < smallest:
	smallest = third_number


print("The Sum =", sum)
print("The Average =", average)
print("The Product =", product)
print("The Smallest =", smallest)


largest = first_number

if second_number > largest and second_number > third_number:
	largest = second_number
elif third_number > second_number and third_number > second_number and third_number > first_number and third_number > largest:
	largest = third_number

print("THe Largest =", largest)