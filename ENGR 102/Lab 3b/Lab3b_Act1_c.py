# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:00:17 2021

@author: user
"""

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name: Ananth Madan
# Section: 7
# Assignment: Lab 3b Act 1a
# Date: 9/15/2021

# This program calculates how much Radon-222 is left given time and initial amount
print('This program calculates how much Radon-222 is left given time and initial amount')
half_life = 3.8
t = float(input('Please enter the time (days): '))
n0 = float(input('Please enter the initial amount (g): '))
print(f'Radon-222 left is {n0*2**(-t/half_life):.02f} g')