# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names: 	Khanh Dao
# 		Ananth Madan
# 		Jerry Kurtin
# 		John Powell
# Section: 219
# Assignment: Lab3a_Act1_c
# Date: 14 September 2021
 
# 1 atm = 760 mm mercury
f = lambda x: x*760
 
num_atm = float(input('Please enter the number of atmospheres to be converted to millimeters of mercury: '))
print(f'{num_atm:.2f} atmospheres is equivalent to {f(num_atm):.2f} millimeters of mercury')
