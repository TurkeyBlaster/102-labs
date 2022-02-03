# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name:		Ananth Madan
# Section: 219
# Assignment: Lab7b_Act1
# Date: 14 October 2021

# a
x = input('What is your name? ')
if x[0].lower() in ['a', 'e', 'i', 'o', 'u']:
	y = x.lower()
else:
	for i in range(1, len(x)):
		if x[i] in ['a', 'e', 'i', 'o', 'u']:
			break
	y = x[i:]
print(f'{x}, {x}, Bo-B{y}')
print(f'Banana-Fana Fo-F{y}')
print(f'Me Mi Mo-M{y}')
print(f'{x}!')