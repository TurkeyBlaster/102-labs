# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Ananth Madan
# Section: 219
# Assignment: Lab11b_P3
# Date: 9 November 2021

def perfect_number(num):
	# The list comprehension does many things in one statement:
	# We iterate over all the numbers from 2 to int(sqrt(n))+1
	# Then, we see if the number is a factor by taking num mod that number
	# If the number is a factor, mod will return 0 (meaning not mod will return 1); otherwise, not
	# If it is a factor, we can add the sum of both it and its complementary factor (since both will be factors)
	# This method is why we don't start at 1
	# However, we also have to check for one in that case
	return num != 1 and num == sum([i+num/i for i in range(2, int(num**0.5)+1) if not num%i]) + 1
