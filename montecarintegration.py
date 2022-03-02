# Python code for Monte Carlo Integration.
# Created By Nikos Avgoustis.

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
plt.style.use("classic")

def func(x):
    return np.sin(x)

def func2d(x,y):
    return np.cos(x)*np.exp(y)
  
a=0
b=np.pi
x = np.linspace(a,b,sampling_num)
y = func(x)
plt.title("Sin(x)")
plt.xlabel("x")
plt.ylabel("Sin(x)")
plt.plot(x,y)
plt.show()

x_min = 0
x_max = np.pi/2
y_min = 0 
y_max = 1
x = np.linspace(x_min, x_max, sampling_num)
y = np.linspace(y_min,y_max,sampling_num)
X, Y = np.meshgrid(x, y)
func = func2d(X,Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, func)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Cos(x)*Exp(y)')
ax.view_init(40,40) 
plt.show()

actual_val = 2
err = []
results = []
for i in range(num_sim):
    r = MonteCarloIntegral(sin,b,1,sampling_num)
    integral = (b-a)*np.mean(r)
    results.append(integral)
    err.append(integral-actual_val)
print("Value Calculated = {} ".format(np.mean(results)))
print("Mean error = {}".format(np.mean(err)))

plt.hist(results)
plt.title("Distribution of Areas Calculated")
plt.xlabel("Areas")
plt.ylabel("Number of Times Calculated")
plt.show()

actual_value2 = 1.71828
results2 = []
err2 = []
for i in range(num_sim):
    r = MonteCarlo2DIntegral(func2d,x_min,x_max,y_min,y_max,sampling_num)
    integral = (x_max-x_min)*(y_max-y_min)*np.mean(r)
    results2.append(integral)
    err2.append(integral-actual_value2)
print("Value Calculated = {} ".format(np.mean(results2)))
print("Mean error = {}".format(np.mean(err2)))

plt.hist(results2)
plt.title("Distribution of Areas Calculated")
plt.xlabel("Areas")
plt.ylabel("Number of Times Calculated")
plt.show()
