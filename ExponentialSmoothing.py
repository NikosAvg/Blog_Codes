# Python code for Exponential Smoothing
# Created By Nikos Avgoustis

import matplotlib.pyplot as plt
import numpy as np
plt.style.use("fivethirtyeight")
plt.rcParams["figure.figsize"] = (20,10)

#Create our data sets
time_steps = 1000

#1. random data from a normal distribution
random_data = np.random.normal(0,1,time_steps)
x1 = np.linspace(0,1,time_steps) 


#Data from a random walk
start = 0
rw = [start]
for i in range(time_steps):
    mv = 1 if np.random.normal(0,1) > 0 else -1
    rw.append(rw[-1] + mv)
    
# 0<a<1
a = 0.2

exp_smooth1 = [random_data[0]]
exp_smooth3 = [rw[0]]


for i in range(1,time_steps):
    exp_smooth1.append(random_data[i]*a + (1-a)*exp_smooth1[-1])
    exp_smooth3.append(rw[i]*a + (1-a)*exp_smooth3[-1])

plt.plot(random_data,label='Random Data')
plt.plot(exp_smooth1,label='Exponential Smoothing a = {}'.format(a))
plt.legend()

plt.plot(rw,label='Random walk')
plt.plot(exp_smooth3, label='Exponential Smoothing a = {}'.format(a))
plt.legend()
