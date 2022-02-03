# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names: 	Khanh Dao
# 		Ananth Madan
# 		Jerry Kurtin
# 		John Powell
# Section: 219
# Assignment: Lab3a_Act1_e
# Date: 14 September 2021
 
# 1 liters per second = 15.8503 gallons per minute
f = lambda x: x*15.8503
 
num_liters_per_sec = float(input('Please enter the number of liters per second to be converted to gallons per minute: '))
print(f'{num_liters_per_sec:.2f} liters per second is equivalent to {f(num_liters_per_sec):.2f} gallons per minute')
 
