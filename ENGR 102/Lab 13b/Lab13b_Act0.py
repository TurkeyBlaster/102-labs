# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Ananth Madan
# Section: 219
# Assignment: Lab13b_Act0
# Date: 1 December 2021
# I have gone through all required sections of the  
# tutorial and understand the material 
import numpy as np
a = np.arange(12).reshape((3, 4))
b = np.arange(8).reshape((4, 2))
c = np.arange(6).reshape((2, 3))
print('A =', a, '\n')
print('B =', b, '\n')
print('C =', c, '\n')
d = a @ b @ c
print('D = ', d, '\n')
print('D^T = ', d.T, '\n')
print('E = ', np.sqrt(d)/2)