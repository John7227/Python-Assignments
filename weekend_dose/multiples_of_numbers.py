number = int(input("Enter a Number: "))

counter = 0
for count in range(1, 100 + 1):
    if count % number == 0:
        counter = counter + 1

print(counter)

