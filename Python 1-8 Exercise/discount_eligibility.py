total_bill = float(input("Enter Total Bill: "))

is_member = input("Are you a Member: ")

discount_rate = 0.0

if total_bill >= 1000 and is_member == "yes":
	discount_rate = 0.10
	print("10% off")
elif total_bill >= 1000 and is_member != "Yes":
	discount_rate = 0.05
	print("5% off")
else:
	print("No discount")

print("The Discount Rate is", discount_rate)

discount_amount = total_bill * discount_rate

final_amount = total_bill - discount_amount

print("The Final Amount is", final_amount)