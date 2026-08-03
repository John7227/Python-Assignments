number = int(input("Enter Number: "))
for count in range(2, number, 1):
    if count % number == 0:
        print(count)
