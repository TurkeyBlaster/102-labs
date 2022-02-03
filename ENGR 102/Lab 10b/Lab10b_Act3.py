# # By submitting this assignment, I agree to the following:
# # "Aggies do not lie, cheat, or steal, or tolerate those who do."
# # "I have not given or received any unauthorized aid on this assignment."
# # Names:   Ananth Madan
# # Section: 219
# # Assignment: Lab10b_Act3
# # Date: 5 November 2021

import csv

# Dict of month ==> (days in month, days before the start of the month)
m_to_int = {'jan': (31, 0),
			'feb': (28, 31),
			'mar': (31, 31+28),
			'apr': (30, 31+28+31),
			'may': (31, 31+28+31+30),
			'jun': (30, 31+28+31+30+31),
			'jul': (31, 31+28+31+30+31+30),
			'aug': (31, 31+28+31+30+31+30+31),
			'sep': (30, 31+28+31+30+31+30+31+31),
			'oct': (31, 31+28+31+30+31+30+31+31+30),
			'nov': (30, 31+28+31+30+31+30+31+31+30+31),
			'dec': (31, 31+28+31+30+31+30+31+31+30+31+30)}

M = input()
m = M.lower()[:3] # Easier to check the first three letters (typing-wise)
d, d_a = m_to_int[m]
Y = int(input())
y = Y-2018 # year ==> 0, 1, or 2
# Leap year
if y == 2:
	if m not in ['jan', 'feb']:
		d_a += 1
	if m == 'feb':
		d += 1
my = d_a+y*365 # Offset for month stats
s = False

m_sum = 0
mp_sum = 0
mw_cnt = 0
min_ = None
max_ = None
p_sum = 0

i = 0

with open('CLLWeatherData.csv', 'r+') as wc:
	wc = csv.reader(wc)
	next(wc)
	for r in wc:
		if i == my and not s: # If we've reached the month we're "stats-ing"
			s = True
		if i == my + d: # When we're past the particular month
			s = False
		if s: # For the days in the month...
			m_sum += float(r[3])
			mp_sum += float(r[2])
			if float(r[1]) > 10:
				mw_cnt += 1
		min_ = min(int(r[-1]), min_) if min_ else int(r[-1])
		max_ = max(int(r[-2]), max_) if max_ else int(r[-2])
		p_sum += float(r[2])
		i += 1
mw_cnt /= d
p_sum /= i
m_sum /= d
mp_sum /= d

print('3-year maximum temperature:', max_, 'F')
print('3-year minimum temperature:', min_, 'F')
print(f'3-year average precipitation: {p_sum:.3f} inches', end='\n\n')
print('Please enter a month: Please enter a year: ') # For Mimir...
print(f'For {M} {Y}:')
print(f'Mean daily temperature: {m_sum:.1f} F')
print(f'Percentage of days with average wind speed above 10 mph: {mw_cnt:.1%}')
print(f'Mean daily precipitation: {mp_sum:.4f} inches')