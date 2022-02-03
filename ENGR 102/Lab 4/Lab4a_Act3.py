# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Khanh Dao
#          Ananth Madan
#          Jerry Kurtin
#          John Powell
# Section: 219
# Assignment: Lab4a_Act3
# Date: 21 September 2021


# Activity 3
########### Part A ###########
bools = []
good = True
def convert_to_bool(b): 
	global good
	if b in ['t', 'T', 'True']:
		return True
	elif b in ['f', 'F', 'False']:
		return False
	else:
		print('Invalid input')
		good = False
		return None

for b in ['a', 'b', 'c']:
	bools.append(convert_to_bool(input(f'Enter True or False for {b}: ')))

########### Part B ###########
if good:
	print(f'a and b and c: {all(bools)}')
	print(f'a or b or c: {any(bools)}')
########### Part C ###########
	print(f'XOR: {bools[0] != bools[1]}')
	print(f'Odd number: {bool(sum(bools)%2)}')
a, b, c = bools

########### Part D ###########

print(f'Complex 1: {(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)}')

print(f'Complex 2: {(not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))}')

print(f'Simple 1: {not b if a else not (b and c)}')
print(f'Simple 2: {a if b else a or c}')