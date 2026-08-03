def palindrome_and_prime_number(given_number):
	if(given_number >= 1 and given_number <= 99999):

		last = given_number % 10
		fourth = (given_number // 10) % 10
		middle = (given_number // 100) % 10
		second = (given_number // 1000) % 10
		first = (given_number // 10000) % 10

		if last == first:
			return "True"

		elif last == first and fourth == second:
			return "True"

		# elif last == last:
		# 	return "True"
		else:
			return "False"
	else:
		return "Make sure your digit is not more than 5!"



given_number = int(input("Enter a Given Number(1-5): "))

print(palindrome_and_prime_number(given_number))



	# public static boolean isPalindrome(int digit) {
	# 	if(digit >= 10000 && digit <= 99999) {

	# 	int last = digit % 10;
	# 	int fourth = digit / 10 % 10;
	# 	int middle = digit / 100 % 10;
	# 	int second = digit / 1000 % 10;
	# 	int first = digit / 10000 % 10;

	# 	if(first == last && second == fourth) {
	# 		return true;
	# 	}
	# 	return false;
		
	# 	}
	# 	System.out.println("Go back and Enter a Five Digit Integer joor!");
	# 	return false;
	# }


 # and given_number % 1 == 0 and given_number % given_number == 0