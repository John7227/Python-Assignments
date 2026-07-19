word = input("Enter a Word: ")

word_length = len(word)


if word_length < 5:
	print("Short string")
elif word_length >= 5 and word_length <= 10:
	print("Medium string")
elif word_length > 10:
	print("Long string")