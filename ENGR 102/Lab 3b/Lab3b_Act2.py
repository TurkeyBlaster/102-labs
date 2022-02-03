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
# Assignment: Lab 3b Act 2
# Date: 9/15/2021

from numpy import pi, sqrt

area = float(input('Please enter the area: '))
# Look, a comment

a2r_c = lambda a: sqrt(a/pi)
a2l_eqt = lambda a: sqrt(4/sqrt(3)*a)
a2l_sq = lambda a: sqrt(a)
a2l_pen = lambda a: sqrt(4*a/sqrt(5*(5+2*sqrt(5))))
a2l_dod = lambda a: sqrt(a/(2+sqrt(3))/3)

print(f'A circle with area {area:.2f} has a radius {a2r_c(area):0>3.3f}')
print(f'An equilateral triangle with area {area:.2f} has a side {a2l_eqt(area):0>3.3f}')
print(f'A square with area {area:.2f} has a side {a2l_sq(area):0>3.3f}')
print(f'A pentagon with area {area:.2f} has a side {a2l_pen(area):0>3.3f}')
print(f'A dodecagon with area {area:.2f} has a side {a2l_dod(area):0>3.3f}')