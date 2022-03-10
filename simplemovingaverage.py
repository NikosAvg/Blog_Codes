# Code for SMA in python
# Created By Nikos Avgoustis

import matplotlib.pyplot as plt
import numpy as np

# Simple moving average
def SMA(data,lag=3):
    sma = []
    for i in range(lag):
        sma.append(np.nan)
    for i in range(lag,len(data)+1):
        sma.append(np.mean(data[i-lag:i]))
    return np.array(sma)

#Create our data sets

#1. random data from a gaussian distribution
random_data = np.random.normal(0,1,100)
x1 = np.linspace(0,1,100) 

#2. Data from a sin function
x2 = np.linspace(0,2*np.pi,100)
y = np.sin(x2)

# Visualize our data
plt.plot(x1,random_data)
plt.title('Random Data')

plt.plot(x2,y)
plt.title('Sinusoid data')


# Calculate sma's lag=3
sma_rand = SMA(random_data)
sma_y = SMA(y)

#Visualize our results
plt.plot(x1,random_data)
plt.plot(x1,sma_rand)
plt.title("SMA for random data \n")

plt.plot(x2,y)
plt.plot(x2,sma_y)
plt.title('SMA for sinusoid data')

plt.show()
