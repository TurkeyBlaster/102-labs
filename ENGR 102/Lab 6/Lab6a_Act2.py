# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Khanh Dao
#          Ananth Madan
#          Jerry Kurtin
#          John Powell
# Section: 219
# Assignment: Lab6a_Act2
# Date: 5 October 2021

# Determines if n is prime
def is_prime(n):
	for i in range(2, int(n**0.5)+1):
		if not n%i:
			return False
	return True

# Loop from 2 through 100
count = 0
for i in range(2, 101):
    print(f'{i} is', end=' ')
    if is_prime(i):
        count += 1
    else:
        print('not', end=' ')
    print('prime')

print(f"There are {count} prime numbers between 2 and 100")