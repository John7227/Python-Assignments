def discount(name_of_item, price_of_item, promotional_code):

	if promotional_code == "SAVE10":
		discount = 0.10
	elif promotional_code == "HALFOFF":
		discount = 0.50
	else:
		discount = price_of_item - (price_of_item * discount)

	discount_price = price_of_item - (price_of_item * discount)

	return discount_price

name_of_item = input("Enter Name of an Item: ")

price_of_item = int(input("Enter the price for " + name_of_item  + ": "))

promotional_code = input("Enter Promotional Code: ")

discount(name_of_item, price_of_item, promotional_code)


print(discount(name_of_item, price_of_item, promotional_code))
