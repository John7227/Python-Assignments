number = int(input("Enter a Number: "))

exponent = 1
for count in range(number):
    exponent *= number
    print(exponent)
