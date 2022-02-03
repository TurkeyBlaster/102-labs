# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name: Ananth Madan
# Section: 7
# Assignment: Lab 4b Act 1
# Date: 9/15/2021

#Lab4b_Act1.py
a = input('Enter number 1: ')
b = input('Enter number 2: ')
c = input('Enter number 3: ')
x = len(a.split('.')[-1]) if len(a.split('.')[-1]) != len(a) else 1
a = float(a)
b = float(b)
c = float(c)
min_ = a
if b < min_:
	min_ = b
if c < min_:
	min_ = c
print(f'The smallest number is {min_:.{x}f}')

