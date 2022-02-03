# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names: 	Khanh Dao
# 		Ananth Madan
# 		Jerry Kurtin
# 		John Powell
# Section: 219
# Assignment: Lab3a_Act1_a
# Date: 14 September 2021

# 1 pound = 4.45 Newtons
f = lambda x: x*4.448
 
num_lbs = float(input("Please enter the number of pounds to be converted to Newtons: "))
print(f"{num_lbs:.2f} pounds is equivalent to {f(num_lbs):.2f} Newtons")
