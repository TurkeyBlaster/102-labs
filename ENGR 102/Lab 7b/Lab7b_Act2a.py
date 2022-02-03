# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name:		Ananth Madan
# Section: 219
# Assignment: Lab7b_Act2
# Date: 14 October 2021

# a
prices = input('Enter three or more prices separated by spaces: ').split()
for price in prices:
	print(f'${price:>7}')