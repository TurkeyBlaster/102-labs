# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Ananth Madan
# Section: 219
# Assignment: Lab13b_Act1
# Date: 1 December 2021
# I have gone through all required sections of the  
# tutorial and understand the material 
import numpy as np
import matplotlib.pyplot as plt
v = np.array([1, 0])
M = np.array([[1.00583, 0.087156], [-0.087156, 1.00583]])
x, y = [v[0]], [v[1]]
for i in range(250):
	v = M @ v
	x.append(v[0])
	y.append(v[1])
plt.plot(x, y, 'b-')
plt.title('Expanding Spiral')
plt.grid(linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.show()