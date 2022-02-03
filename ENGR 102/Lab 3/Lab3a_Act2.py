# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names: 	Khanh Dao
# 		Ananth Madan
# 		Jerry Kurtin
# 		John Powell
# Section: 219
# Assignment: Lab3a_Act2
# Date: 14 September 2021
 
def interpolate(p1, p2):
   # Find the step size between times
   step_t = (p2[3] - p1[3]) / 4
   print()
   for i in range(5):
       arr  = []
       for j in range(3):
           slope = (p2[j] - p1[j])/(p2[3] - p1[3])
           arr.append(slope)
       time_increment = i * step_t
       print("At time {time:.1f} seconds the object is at ({x_val:.2f}, {y_val:.2f}, {z_val:.2f})".format(time=time_increment+p1[3], x_val=arr[0]*time_increment+p1[0], y_val=arr[1]*time_increment+p1[1], z_val=arr[2]*time_increment+p1[2]))

t1 = input('Enter time 1: ')
x1 = input('Enter the x position of the object at time 1: ')
y1 = input('Enter the y position of the object at time 1: ')
z1 = input('Enter the z position of the object at time 1: ')

t2 = input('Enter time 2: ')
x2 = input('Enter the x position of the object at time 2: ')
y2 = input('Enter the y position of the object at time 2: ')
z2 = input('Enter the z position of the object at time 2: ')

p1_str = [x1, y1, z1, t1]
p2_str = [x2, y2, z2, t2]

p1 = [float(i) for i in p1_str]  # converts all the input to float with
p2 = [float(i) for i in p2_str]  # list comprehension

interpolate(p1, p2)
