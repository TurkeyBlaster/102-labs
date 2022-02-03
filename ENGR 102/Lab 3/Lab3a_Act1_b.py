# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names: 	Khanh Dao
# 		Ananth Madan
# 		Jerry Kurtin
# 		John Powell
# Section: 219
# Assignment: Lab3a_Act1_b
# Date: 14 September 2021
 
# 1 km = 0.62137 miles
f = lambda x: x * 0.62137
 
num_kiloms = float(input('Please enter the number of kilometers to be converted to miles: '))
print(f'{num_kiloms:.2f} kilometers is equivalent to {f(num_kiloms):.2f} miles')
