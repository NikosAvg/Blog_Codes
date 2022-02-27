# Python code for 2D Random Walk
# Created By Nikos Avgoustis

import matplotlib.pyplot as plt
import numpy as np

#initialize coordinate and probabilities
x=[0]
y=[0]
steps = 1000
probability = np.random.randint(0,5,steps)

#loop through our list of probabilities and build the walk
for p in probability:
    if p == 0:
        x.append(x[-1]+1)
        y.append(y[-1])
    elif p == 1:
        x.append(x[-1]-1)
        y.append(y[-1])
    elif p == 2:
        y.append(y[-1]+1)
        x.append(x[-1])
    elif p == 3:
        y.append(y[-1]-1)
        x.append(x[-1])
        
plt.plot(y,x)
plt.title('2D Random Walk')
plt.xlabel('X-Axis Coordinate')
plt.ylabel('Y-Axis Coordinate')
