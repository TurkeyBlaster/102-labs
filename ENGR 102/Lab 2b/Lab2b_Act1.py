# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name: Ananth Madan
# Section: 7
# Assignment: Lab 2b Act 1
# Date: 9/14/2021

# Lab 1
from numpy import sin, pi
# --------------------------
mass = 2
acceleration = 5
force = mass * acceleration
print(f'Force is {force} N')
# ---------------------------
n = 1
d = 0.025
theta = 25
print(f'Wavelength is {2*d*sin(pi*theta/180)/n} nm')
# --------------------------------------------------
n0 = 3
half_life = 3.8
t = 5
print(f'Radon-222 left is {n0*2**(-t/half_life)} g')
# ---------------------------------------------------
p = 0.15
n = 5
r = 8.314
t = 425
print(f'Pressure is {n*r*t/p/1000} kPa')