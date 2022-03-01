# Python code for Monte Carlo simulation of a dice game.
# Created by Nikos Avgoustis.

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('classic')

# The function that simulates a dice roll
def diceRoll():
    return np.random.randint(1,7)

# The function that simulates a player
def player(bet,dice_result):
  if bet == dice_result:
      return True
  return False

# The function that will run the simulation
def Simulation(initial_position,num_simulations,bet_number,bet_amount,num_of_bets):
    results = []
    for n in range(num_simulations):
        y = [initial_position]
        for i in range(num_of_bets):
            dice = diceRoll()
            if player(diceRoll(),bet):
                y.append(y[-1]+bet_amount)
            else:
                y.append(y[-1]-bet_amount)
        results.append(y)
    return results
  
  # Initialize our parammeters
num_simulations = 1000
initial_position = 10000
num_of_bets = 100
bet_number = 3
bet_amount = 100

# Run the simulation.
results = Simulation(initial_position,num_simulations,bet_number,bet_amount,num_of_bets)

# Visualize our results with line plots
x = list(range(num_of_bets+1))
end_value = [y[-1] for y in results]
mean_end_value = np.mean(end_value)
for y in results:
    plt.plot(x,y)
    
plt.xlabel("Number of bets")
plt.ylabel("Position")
plt.title("Monte Carlo Simulation of {} dice rolls \n (Mean End Amount = {})".format(num_of_bets,mean_end_value))
plt.show()

# Visualize our results with a histogram
plt.hist(end_value,density=True)
plt.xlabel("Final amounts")
plt.ylabel("Probability")
plt.title("Histogram of our Final amounts")
plt.show()
