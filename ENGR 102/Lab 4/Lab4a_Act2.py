# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Khanh Dao
#          Ananth Madan
#          Jerry Kurtin
#          John Powell
# Section: 219
# Assignment: Lab4a_Act2
# Date: 21 September 2021
# Activity 2
a = int(input('Please enter the coefficient A: '))
b = int(input('Please enter the coefficient B: '))
c = int(input('Please enter the coefficient C: '))
sign = lambda x, i: '+ ' if x>0 and i else '- ' if x<0 else ''
str_coeff = lambda x: str(x) if abs(x) != 1 else ''
str_var = lambda x, y, i: f'{sign(x, i)}{str_coeff(abs(x))}{y} ' if x != 0 else ''
print(f"The quadratic equation is {str_var(a, 'x^2', 0)}{str_var(b, 'x', a!=0)}{str_var(c, '', b!=0 or a!=0)}= 0")