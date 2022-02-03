# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names: 	Khanh Dao
# 		Ananth Madan
# 		Jerry Kurtin
# 		John Powell
# Section: 219
# Assignment: Lab3a_Act1_f
# Date: 14 September 2021
 
# 1 degree Celsius = 493.47 degrees Rankine
f = lambda x: 9/5*x + 491.67
 
deg_celsius = float(input('Please enter the number of degrees Celsius to be converted to degrees Rankine: '))
print(f'{deg_celsius:.2f} degrees Celsius is equivalent to {f(deg_celsius):.2f} degrees Rankine')
 
 
