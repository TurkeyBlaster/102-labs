# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name: Ananth Madan
# Section: 7
# Assignment: Lab 2b Act 2c
# Date: 9/14/2021
# Lab 2c
import numpy as np
t1 = 30
t2 = 60
t_step = (t2-t1)/(5-1)
v = (np.array([25, -5, 11])-np.array([2, 3, 7]))/(85-12)
p2 = v*(t1-12)+np.array([2, 3, 7])
for i in range(5):
    if i == 0:
        print('At time 30 seconds:')
    elif i == 4:
        print('At time 60 seconds:')
    else:
        print(f'At time {t1+t_step*i} seconds:')
    print(f'x0 = {p2[0]} m\ny0 = {p2[1]} m\nz0 = {p2[2]} m')
    if i != 4:
        print('----------------------')
    p2 += t_step*v