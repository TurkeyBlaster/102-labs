# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name: Ananth Madan
# Section: 7
# Assignment: Lab 4b Act 4
# Date: 9/15/2021

#Lab4b_Act4.py
a = float(input('Please enter the coefficient A: '))
b = float(input('Please enter the coefficient B: '))
c = float(input('Please enter the coefficient C: '))

if a:
	D=b**2-4*a*c
	if D > 0:
		D **= 1/2
		D *= 1/(2*a)
		b *= -1/(2*a)
		print(f'The roots are x = {b+D:.1f} and x = {b-D:.1f}')
	elif D < 0:
		D *= -1
		D **= 1/2
		D *= 1/(2*a)
		b *= -1/(2*a)
		print(f'The roots are x = {b} + {D:.1f}i and x = {b} - {D:.1f}i')
	else:
		print(f'The root is x = {-b/(2*a)}')
elif b:
	print(f'The root is x = {-c/b}')
else:
	print('You entered an invalid combination of coefficients')