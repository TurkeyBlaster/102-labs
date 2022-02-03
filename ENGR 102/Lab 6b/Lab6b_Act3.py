# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Ananth Madan
# Section: 219
# Assignment: Lab6b_Act3
# Date: 8 October 2021

import numpy as np
from matplotlib import pyplot as plt
x = 202.4
v = float(input("What's the initial velocity? "))
g = 9.80665
theta = 0
y = 1
rat = 1
# Newton's Method
while rat > 0.05:
	f = -y + x*np.tan(theta) - (g*x**2)/(2*(v*np.cos(theta))**2)
	f_p = -1/(np.cos(theta)**2) * ((g*x**2*np.tan(theta))/(v**2) - x)
	rat = np.abs(f/f_p)
	theta -= f/f_p

if 0 < theta <= np.pi/2:
	X = np.arange(0, x, 0.01)
	Y = X*np.tan(theta) - g*X**2/(2*v**2*np.cos(theta)**2)
	plt.plot(X, Y)
	plt.show(block=False)
	y_mars = x*np.tan(theta) - 3.72076*x**2/(2*v**2*np.cos(theta)**2)
	print(f"Angle: {theta*180/np.pi} deg")
	print(f"Height of impact on Earth: {Y[-1]}")
	print(f"Height of impact on Mars: {y_mars}")
else:
	print("No solution")