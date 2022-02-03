# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Ananth Madan
# Section: 219
# Assignment: Lab11b_P1
# Date: 9 November 2021

import numpy as np

def min_profit(f, c, v):
	'''
	Finds the least profitable facility based on `c` and `v`
	
	Parameters
	----------
	f : list
		Facility names
	c : list
		Annual cost per facility
		Should have same length as f
	v : list
		Annual value produced per facility
		Should have same length as f
	
	Returns
	-------
	tuple
		Name of facility with lowest annual profit,
		Net profitability of said facility
	'''
	p = np.subtract(v, c) # profit
	i = np.argmin(p) # Find argmin of v-c
	return f[i], p[i]