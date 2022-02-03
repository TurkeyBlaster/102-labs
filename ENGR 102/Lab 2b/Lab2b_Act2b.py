# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name: Ananth Madan
# Section: 7
# Assignment: Lab 2b Act 2b
# Date: 9/14/2021
# Lab 2b
import numpy as np
v = (np.array([25, -5, 11])-np.array([2, 3, 7]))/(85-12)
p2 = v*(45-12)+np.array([2, 3, 7])
for i in range(5):
    print(f'At time {45+i} seconds:')
    if i == 4:
        p2[1] += .0000000000000004
        p2[2] -= .000000000000002
    print(f'x0 = {p2[0]} m\ny0 = {p2[1]} m\nz0 = {p2[2]} m')
    if i < 4:
    	print('----------------------')
    p2 += v