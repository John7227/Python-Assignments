name = input("Enter Name: ")

name_length = len(name)

if name_length >= 0 and name_length <= 5:
	print("Hi",name)
else:
	print("Hello",name)