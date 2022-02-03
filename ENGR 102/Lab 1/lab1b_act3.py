from numpy import exp
# Lab 3
# Prints things
print('This shows the evaluation of (e^x-1)/x evaluated close to x=0')
func = lambda x: (exp(x)-1)/x
print(f'My guess is {func(1.1)}')
for i in range(8):
	print(f'{func(10**-i):.12f}')
print()
print('Finished')
print()