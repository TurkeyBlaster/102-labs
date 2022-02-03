# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
# Names:   Khanh Dao
#          Ananth Madan
#          Jerry Kurtin
#          John Powell
# Section: 219
# Assignment: Lab8Act1
# Date: 19 October 2021

from math import exp
import matplotlib.pyplot as plt

#### Figure 1 ####
t = [0, 0.45, 1.1, 1.75, 2.25, 2.7] # t values
y = [0, 0.23, 0.4, 0.18, 0.07, 0.01] # y values
x = [] # domain of the curves (the points used to plots them)
f1 = [] # curve 1
f2 = [] # curve 2

# finds y values for function 1. 0 <= x <= 3
for i in range(0, 61):
    i /= 20
    x.append(i)
    f1.append((i ** 2) * exp(-(i ** 2)))
    
# finds y values for function 2. 0 <= x <= 3
for i in range(0, 61):
    i /= 20
    f2.append((i ** 4) * exp(-(i ** 2)))


#### Display ####
# Figure 1
plt.subplot(2, 1, 1)

plt.plot(t, y, "ko", label="data") # The data points
plt.plot(x, f1, color="red", linestyle="-", label = "t^2*exp(-t^2)") # Curve 1
plt.plot(x, f2, color="blue", linestyle="-", label = "t^4*exp(-t^2)") # Curve 2

plt.legend(loc='upper right')  # Plot the legend in the upper right
plt.title("Data and two curves vs. time") # Title
plt.axis([0.0, 3.0, 0.0, 1.0]) # limit the axes
plt.xlabel("time") # x-axis label
plt.ylabel("y") # y-axis label
plt.xticks([0.0, 0.5, 1.0, 1.5, 2.0, 2.5]) # appropriate ticks
plt.yticks([i/10 for i in range(0, 11, 2)])  # returns list 0.0-1.0 inclusive (increments of 0.2)

# Figure 2
plt.subplot(2, 1, 2)

# plots function yellow triangle and line(data)
plt.plot(t, y, "y-") # 
plt.plot(t, y, "y^",label="data")
plt.plot(x, f1, color="blue", linestyle="-", label = "t^2*exp(-t^2)")

# "it's closest here" and the arrow
x_pt = 1.4
plt.annotate("It's closest here!", xy=(x_pt, (x_pt ** 2) * exp(-( x_pt** 2))), xycoords='data', xytext=(-70, -20), textcoords="offset points", fontsize=9, arrowprops={'arrowstyle': "->"})


plt.legend(loc='upper right') # plot the legend in the upper right
plt.title("Data interpolation and Curve 1") # appropriate title
plt.axis([1.0, 2.0, 0.0, 0.5]) # limit the axes
plt.xlabel("time") # x-axis label
plt.ylabel("y") # y-axis label
plt.xticks([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
plt.yticks([i/10 for i in range(6)])  # returns list 0.0-0.5 inclusive (increments of 0.1)

# Prevent overlap and display graph
plt.tight_layout()
plt.show()