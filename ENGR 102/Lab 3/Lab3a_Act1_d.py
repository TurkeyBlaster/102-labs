# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names: 	Khanh Dao
# 		Ananth Madan
# 		Jerry Kurtin
# 		John Powell
# Section: 219
# Assignment: Lab3a_Act1_d
# Date: 14 September 2021
 
# 1 watt = 3.41 BTU per hour
f = lambda x: x*3.41214
 
num_watts = float(input('Please enter the number of watts to be converted to BTU per hour: '))
print(f'{num_watts:.2f} watts is equivalent to {f(num_watts):.2f} BTU per hour')
