number = input("Enter a Binary Number: ")
length = len(number) - 1
decimal_sum = 0
for count in number:
	decimal_sum += int(count) * 2 ** length
	length = length - 1
	print(decimal_sum)