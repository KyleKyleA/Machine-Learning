import numpy as np 
import matplotlib.pyplot as plt
import timeit

high_var = np.array([1, 100, 200, 300, 4000, 5000])
low_var = np.array([2, 4, 6, 8, 10])

# Printing variance
print(np.var(high_var), np.var(low_var))

# Printing standard deviation which is the square root of the variance
print (np.std(high_var), np.std(low_var))

# Printing the value of the standard deviation of the high variance array by taking the square root of the variance
print(np.sqrt(np.var(high_var)))

# Matplotlib 
plt.hist(high_var)
plt.show()

# Showing low variance array with a histogram 
plt.hist(low_var)
plt.show()

timeit.timeit(lambda: np.var(high_var), number=1000000)
