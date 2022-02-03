# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Ananth Madan
# Section: 219
# Assignment: Lab11b_P2
# Date: 9 November 2021

def mailing_list():
	# Prompt user for information
	name = input('Name: ')
	city = input('City: ')
	state = input('State: ')
	zip = input('Zip code: ')
	addr = input('Address: ')
	# Get input for second line
	a = input('')
	if a: # if input for second line consists of something
		addr = f'{addr}\n{a}' # add it to a (with a newline)
	# Print everything (in the format specified)
	print(name)
	print(addr)
	print(city, ',', state, zip)
