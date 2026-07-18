#Collect current father age from the user
#Collect current son age from the user
#Then get the twice age of the son which will be current age of the son plus current age of the son
#Then I will get the father twice age which will be the current father age minus the twice son age, I got the son's #twice age.
#What if x2 of the son's age is older than the father that will give me a minus that is where an if statement comes #in which will be if the twice father age is lower than 0 print the current age of the son plus the current age of #the son
#Else print the one we did before

current_father_age = int(input("Enter Current Father's Age: "))

current_son_age = int(input("Enter Current Son's Age: "))

twice_son_sge = int(current_son_age + current_son_age)

father_twice_as_old_as_his_son = int(current_father_age - twice_son_sge)

age_father_will_be = int(twice_son_sge - current_father_age)

if father_twice_as_old_as_his_son < 0:
	print("In", age_father_will_be, "Years, his father will becomes twice the age of his Son")

else:
	print(father_twice_as_old_as_his_son," Years ago, the father was twice as old as the Son" )
