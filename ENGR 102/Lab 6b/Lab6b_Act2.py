# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Ananth Madan
# Section: 219
# Assignment: Lab6b_Act2
# Date: 8 October 2021

for i in range(2, 101):
	for j in range(2, i+1):
		if j%i == 0: # Check divisibility
			print(f'{i} divides {j}')