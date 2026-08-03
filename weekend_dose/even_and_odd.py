number = int(input("Enter a Number: "))

counter = 0
counters = 0
for count in range(1, number + 1):
    if count % 2 == 0:
        counter = counter + 1
    elif count % 2 != 0:
        counters = counters + 1    

print("Even Numbers" , "=", counter)
print("Odd Numbers" , "=", counters)
