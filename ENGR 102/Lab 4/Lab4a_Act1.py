# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Khanh Dao
#          Ananth Madan
#          Jerry Kurtin
#          John Powell
# Section: 219
# Assignment: Lab4a_Act1
# Date: 21 September 2021

from math import ceil
print('Enter the hours parked as a decimal number. Include a negative sign if the ticket is lost.')
# Convert hours to float
hours = float(input('Please enter the hours parked: '))

if hours < 0:  # lost ticket
    charge = 36
    hrs = abs(hours)
else:
    hrs = hours
    charge = 0

# find the remainder of hours
days, hrs = divmod(hrs, 24)
charge += 24*days + min(24, 4 * (hrs > 0) + 3 * (hrs > 2) + ceil(hrs - 4) * (hrs > 4))
print(f'Parking for {hours} hours please pay ${int(charge)}')