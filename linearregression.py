# Python code for Simple Linear Regression
# Created By Nikos Avgoustis

import numpy as np
import matplotlib.pyplot as plt
plt.style.use("classic")

# Create a function to generate datasets

def create_dataset(num_points,variance,step=2,correlation=False):
	val = 1
	ys = []
	for i in range(num_points):
		y = val + np.random.randint(-variance, variance)
		ys.append(y)
		if correlation and correlation=='pos':
			val+=step
		elif correlation and correlation=='neg':
			val-=step

	x = [i for i in range(len(ys))]

	return np.array(x,dtype=np.float64), np.array(ys,dtype=np.float64)

# Create and visualize our datasets
xs, ys = create_dataset(100,50,2,correlation='pos') 
plt.scatter(xs,ys,'o')
plt.xlabel("Input variable (X)")
plt.ylabel("Output variable (Y)")
plt.title("Our Dataset")
plt.show()

# Create the functions to calculate the best parameters a and b and calculate the R-Squared metric.
def best_fit_slope_intercept(x,y):
	a = ( ((np.mean(x)*np.mean(y)) - np.mean(x*y)) /
			((np.mean(x)*np.mean(x)) - np.mean(x*x)))
	b = np.mean(y) - a* np.mean(x)
	return a, b

def squared_error(y_orig, y_line):
	return np.sum((y_line - y_orig)**2)
		
def coefficient_of_determination(y_orig,y_line):
	y_mean_line = [np.mean(y_orig) for y in y_orig]	
	squared_error_reg = squared_error(y_orig, y_line)
	squared_error_y_mean = squared_error(y_orig, y_mean_line)
	return 1-(squared_error_reg/squared_error_y_mean)

# Run the algorithm and visualize teh results.
a, b = best_fit_slope_intercept(xs,ys)

regression_line = [(a*x)+b for x in xs]
rsq = coefficient_of_determination(ys,regression_line)

plt.scatter(xs,ys,color="g",label="Data Points")
plt.plot(xs,regression_line,color="r",label="Best Fit line")
plt.title("Linear Regression Results (Best Fit Line)\n R-Squared Error = {}".format(np.round(rsq,3)))
plt.xlabel("Input variable (X)")
plt.ylabel("Output variable (Y)")
plt.legend(loc="best")
plt.show()
