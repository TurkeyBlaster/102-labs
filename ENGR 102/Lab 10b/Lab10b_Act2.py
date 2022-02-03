# # By submitting this assignment, I agree to the following:
# # "Aggies do not lie, cheat, or steal, or tolerate those who do."
# # "I have not given or received any unauthorized aid on this assignment."
# # Names:   Ananth Madan
# # Section: 219
# # Assignment: Lab10b_Act2
# # Date: 5 November 2021

import csv

out = input('Please enter the output filename: ')
P = int(input('Please enter the principal amount: '))
N = int(input('Please enter the term length (months): '))
i = float(input('Please enter the annual interest rate: '))
J = i/12 # Monthly interest rate
i_t = 0
M = P*J/(1-(1/(1+J)**N)) # Monthly update

with open(out, 'w', newline='') as out:
	out = csv.writer(out, delimiter=',')
	out.writerow(['Month','Total Accrued Interest','Loan Balance'])
	out.writerow([f'{i}', f'${i_t:.2f}', f'${P:.2f}'])
	for i in range(1, N+1):
		i_t += P*J # Add accured interest rate
		P *= (1+J) # Equal to P += P*J
		P -= M # Subtract monthly payment
		if P < 0.01: # Break condition
			# min accounts for if principal is less than zero
			out.writerow([f'{i}', f'${i_t:.2f}', f'${min(0, P):.2f}'])
			break
		else:
			out.writerow([f'{i}', f'${i_t:.2f}', f'${P:.2f}'])