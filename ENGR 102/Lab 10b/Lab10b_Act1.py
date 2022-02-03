# # By submitting this assignment, I agree to the following:
# # "Aggies do not lie, cheat, or steal, or tolerate those who do."
# # "I have not given or received any unauthorized aid on this assignment."
# # Names:   Ananth Madan
# # Section: 219
# # Assignment: Lab10b_Act1
# # Date: 5 November 2021

coins = 0
with open('coins.txt', 'w') as c_f: # writing coins.txt
	with open('game.txt', 'r') as g: # reading game.txt
		lines = g.readlines() # file ==> list
		l = 0
		while 0 <= l < len(lines): # Assert instructions are in bounds
			line = lines[l] # Current line
			if line[:4] == 'coin': # If 'coin'
				c = int(line[5:]) # Add to coin total
				coins += c
				c_f.write(str(c)) # Write updates to coins.txt
				c_f.write('\n')
			elif line[:4] == 'jump': # If jump
				l += int(line[5:]) # jump to particular line
				continue
			l += 1 # increment line (only executes if jump doesn't)
print('Total coins:', coins)