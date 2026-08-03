counter = 0
total = 0
for count in range(10):
    number = int(input("Enter Number:"))
    counter = counter + 1
    total = total + number

average = total / counter
print(average)
