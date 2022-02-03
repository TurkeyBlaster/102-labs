# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Khanh Dao
#          Ananth Madan
#          Jerry Kurtin
#          John Powell
# Section: 219
# Assignment: Lab6a_Act1b
# Date: 5 October 2021

# Input for side length and n
s = float(input("Enter the side length in meters: "))
n = int(input("Enter the number of layers: "))

area = s**2*(1+3*(n-1)*(n>1)+(n-2)*(n-1)*(n>2)+2*n*(n+1))

print(f'You need {area:.2f} square meters of gold foil to cover the pyramid')