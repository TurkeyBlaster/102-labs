# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name: Ananth Madan
# Section: 7
# Assignment: Lab 3b Act 1a
# Date: 9/15/2021

# This program calculates the applied force given mass and acceleration
print('This program calculates the applied force given mass and acceleration')
mass = float(input('Please enter the mass (kg): '))
acceleration = float(input('Please enter the acceleration (m/s^2): '))
force = mass * acceleration
print(f'Force is {force:.1f} N')
