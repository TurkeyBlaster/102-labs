# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Khanh Dao
#          Ananth Madan
#          Jerry Kurtin
#          John Powell
# Section: 219
# Assignment: Lab5b_Act2
# Date: 30 September 2021

import numpy as np

i = float(input('Enter the strain: ')) # Get user input

if i > 0.27 or i < 0: # The graph is only defined in the region [0, 0.27]
	print('Strain is undefined in that region')
	stress = None
# Use else-ifs to determine with line the region falls into
# Then, use y=mx+b to calculate an appropriate approximation
elif i >= 0.18:
	stress = -9/0.09*(i-0.18)+60
elif i >= 0.06:
	stress = 16.5/0.12*(i-0.06)+43.5
elif i >= 0.01:
	stress = 0.5/0.05*(i-0.01)+43
else:
	stress = 43/0.01*i

# Output result
if stress is not None: # Don't output anything if strain is None
	print(f'The stress is approximately {stress:.1f}')