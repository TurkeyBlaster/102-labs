# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Ananth Madan
# Section: 219
# Assignment: Lab6b_Act1
# Date: 8 October 2021

sum = count = min = max = elem = 0
while True:
	# Validate input
	try:
		elem = float(input("Enter measurement: "))
	except ValueError:
		print('Illegal value: must be a float.')
		continue
	if elem < 0:
		break
	sum += elem
	count += 1
	if elem < min or count == 0:
		min = elem
	if elem > max or count == 0:
		max = elem
	
# output
print(f'Max: {max}')
print(f'Min: {min}')
print(f'Mean: {sum/count}')