largest = input("Enter First Number: ")
second_number = input("Enter Second Number: ")
third_number = input("Enter Third Number: ")


if second_number > largest and second_number > third_number:
	largest = second_number

if third_number > largest and third_number > second_number:
	largest = third_number

print("The Largest is", largest)





#if largest < second_number and largest < third_number:
#	largest = second_number
#
#if largest < third_number:
#	largest = third_number
#
#print("The Largest is", largest)
