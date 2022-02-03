# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:00:16 2021

@author: user
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name: Ananth Madan
# Section: 7
# Assignment: Lab 3b Act 1b
# Date: 9/15/2021

from numpy import sin, pi
# This program calculates the wavelength given distance and angle
print('This program calculates the wavelength given distance and angle')
n = 1
d = float(input('Please enter the distance (nm): '))
theta = float(input('Please enter the angle (degrees): '))
print(f'Wavelength is {2*d*sin(pi*theta/180)/n:.04f} nm')