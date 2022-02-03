# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name: Ananth Madan
# Section: 7
# Assignment: Lab 2b Act 2a
# Date: 9/14/2021
# Lab 2a
import numpy as np
def lerp(p0, p1, t0, t1, t):
	p2=(p1-p0)/(t1-t0)*(t-t0)+p0
	return f'x0 = {p2[0]} m\ny0 = {p2[1]} m\nz0 = {p2[2]} m'
print('At time 45 seconds:')
print(lerp(np.array([2, 3, 7]), np.array([25, -5, 11]), 12, 85, 45))