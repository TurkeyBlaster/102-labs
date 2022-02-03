# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name: Ananth Madan
# Section: 7
# Assignment: Lab 4b Act 3
# Date: 9/15/2021

#Lab4b_Act3.py
days = input('Please enter a positive value for day: ')
good = False
if days.isdigit():
	days = int(days)
	if days >= 0:
		print(f'The total number of widgets produced on day {days} is {10*min(days, 50) + min(days-10, 40)*min(days-9, 41)//2*(days>10) + 50*min(50, days-50)*(days>50)}')
		good = True
		
if not good:
	print('You entered an invalid number!')