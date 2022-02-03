# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Khanh Dao
#          Ananth Madan
#          Jerry Kurtin
#          John Powell
# Section: 219
# Assignment: Lab6a_Act1a
# Date: 5 October 2021

# Get side length and n layers
length = float(input("Enter the side length in meters: "))
n = int(input("Enter the number of layers: "))

area = 0  # Surface area of gold needed
A = length ** 2  # Area of a single square

for layer in range(n, 2, -1):
    # Side area
    area += layer * A
    # Top area
    area += 1/2 * A * (layer-2) + 3/4 * A

if n != 1:  # Edge case needs special treatment :)
    # Layer 2
    area += 3/4 * A + 2 * A
    
# Layer 1
area += 5/4 * A
area *= 4  # for all 4 sides of the pyramid


print(f'You need {area:.2f} square meters of gold foil to cover the pyramid')
