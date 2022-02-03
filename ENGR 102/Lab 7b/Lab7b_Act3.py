# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Name:		Ananth Madan
# Section: 219
# Assignment: Lab7b_Act3
# Date: 14 October 2021

# a
a = list(map(float, input("Enter the elements for vector A: ").split()))
b = list(map(float, input("Enter the elements for vector B: ").split()))
print(f"The magnitude of vector A is {sum(map(lambda x:x**2, a))**0.5:.4f}")
print(f"The magnitude of vector B is {sum(map(lambda x:x**2, b))**0.5:.4f}")
print(f"A + B is {[a[i]+b[i] for i in range(len(a))]}")
print(f"A - B is {[a[i]-b[i] for i in range(len(a))]}")
print(f"The dot product is {sum([a[i]*b[i] for i in range(len(a))])}")