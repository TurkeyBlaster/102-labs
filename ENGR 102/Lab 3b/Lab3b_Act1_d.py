# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:00:18 2021

@author: user
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name: Ananth Madan
# Section: 7
# Assignment: Lab 3b Act 1a
# Date: 9/15/2021

# This program calculates the pressure given moles, volume, and temperature
print('This program calculates the pressure given moles, volume, and temperature')
n = float(input('Please enter the number of moles: '))
v = float(input('Please enter the volume (m^3): '))
r = 8.314
t = float(input('Please enter the temperature (K): '))
print(f'Pressure is {n*r*t/v/1000:.0f} kPa')