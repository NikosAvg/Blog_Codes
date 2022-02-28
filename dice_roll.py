# Python code for Dice roll simulation
# Created By Nikos Avgoustis

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('classic')

def diceRoll():
    return np.random.randint(1,7)
  
  
number_of_rolls = 10000

results = []
for i in range(number_of_rolls):
    results.append(diceRoll())
    
plt.hist(results,density=True,bins = 6)
plt.xlabel("Possible Outcomes")
plt.ylabel("Probability")
plt.title("Probability of Dice throw results")
    
results2 = []
for i in range(number_of_rolls):
    results2.append(diceRoll()+diceRoll())
    
plt.hist(results2,density=True,bins=11)
plt.xlabel("Possible Outcomes")
plt.ylabel("Probability")
plt.title("Probability of The Sum of Two Dice")
plt.show()
