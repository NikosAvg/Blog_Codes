# Python code for 1D Random Walk
# Created By Nikos Avgoustis

import numpy as np
import matplotlib.pyplot as plt

#Initialize the list and set the first point at 0
random_walk = [0]

# Initialize the number of steps and generate the random numbers with 50% chance
steps = 100
random_numbers = np.random.randint(0,2,steps)

# Loop through the numbers and create the random walk
# If the number is 0 we add 1 to our previous position else we subtract 1.
for r in random_numbers:
    if r == 0:
        step=1
    else:
        step=-1
    random_walk.append(random_walk[-1]+step)

# Visualize the Random Walk
plt.plot(random_walk)
plt.title("Simple Random Walk")
plt.xlabel("Time steps")
plt.ylabel("Current Position")
plt.show()