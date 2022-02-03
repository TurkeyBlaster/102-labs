# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names: Khanh Dao
# Ananth Madan
# Jerry Kurtin
# John Powell
# Section: 219
# Assignment: Lab2a_Act3
# Date: 9 September 2021

from numpy import pi

print('Part 1:')
lerp = lambda d1, d2, t1, t2, t: (d2-d1)/(t2-t1)*(t-t1)+d1
print(f'For t = 25 minutes, the position p = {lerp(2025, 23025, 10, 55, 25)} kilometers')

print('Part 2:')
clerp = lambda d1, d2, t1, t2, t, r: lerp(d1, d2, t1, t2, t)%(2*pi*r)
print(f'For t = 5.0 hours, the position p = {clerp(2025, 23025, 10, 55, 300, 6745)} kilometers')