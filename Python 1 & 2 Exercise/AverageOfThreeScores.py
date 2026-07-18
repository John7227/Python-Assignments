#Collect the first Score from the user
#Collect the second Score from the user
#Collect the third Score from the user
#Then get the total of the scores which will addition of the three scores
#Then get the average which will be the total divided by 3
#Then if the average falls between the range of 90 to 100 it should print A
#If the average falls between the range of 80 to 90 it should print B
#If the average falls between the range of 70 to 80 it should print C
#If the average falls between the range of 60 to 70 it should print D
#If the average falls between the range of 0 to 60 it should print F


first_score = int(input("Enter First Score: "))

second_score = int(input("Enter Second Score: "))

third_score = int(input("Enter Third Score: "))

total_score = int(first_score + second_score + third_score)

average = int(total_score / 3)

print("The Total is", total_score)

if average >= 90 and average <= 100:
	print("A")
elif average >= 80 and average < 90:
	print("B")
elif average >= 70 and average < 80:
	print("C")
elif average >= 60 and average < 70:
	print("D")
elif average >= 0 and average < 60:
	print("F")