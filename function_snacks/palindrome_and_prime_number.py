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















def check_number(number):
    # 1. Check for Palindrome
    num_str = str(number)
    is_palindrome = num_str == num_str[::-1]

    # 2. Check for Prime
    is_prime = True
    if number <= 1:
        is_prime = False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break  # Stop looping immediately if we find a factor

    # Return both results together
    return is_palindrome, is_prime


def run_test(user_number):
    # Call the main function and get both results at once
    palindrome_result, prime_result = check_number(user_number)

    # Print the results nicely
    print(f"Results for {user_number}:")
    print(f"- Is it a palindrome? {palindrome_result}")
    print(f"- Is it a prime number? {prime_result}")
    print("-" * 25)  # Visual separator line













