# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name: Ananth Madan
# Section: 7
# Assignment: Lab 3b Challenge
# Date: 9/15/2021

from numpy import pi
pi_to_x = lambda x: f'{pi:.{x}f}'
x = int(input('Please enter the number of digits of precision for pi: '))
print(f'The value of pi to {x} digits is: {pi_to_x(x)}')