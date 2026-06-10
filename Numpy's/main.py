from timeit import timeit
import time 
import numpy as np


# Print version of numpy
print(np.__version__)

# Printing 1 dimensional array that only prints in a single line 
a1 = np.array([1,3,5])
print(a1)

# Printing multi dimesional array that prints in multiple lines called matrix's 
# goes by row by row, column by column 
a2 = np.array([[1, 2.0, 3], [4, 5, 6]])
print(a2)

# Another example but much larger and goes 3 x 3 x 3 and is a 3 dimensional array
a3 = np.array([[[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]],
                [[10, 11, 12],
                 [13, 14, 15],
                 [16, 17, 18]]])
print(a3)

# Goes so on and so forth.


# pandas Dataframe out of the Numpy array 
import pandas as pd

df = pd.DataFrame(np.random.randint(10, size=(5, 5)),
                  columns=['A', 'B', 'C', 'D', 'E'])
print(df)

# 2.) creating arrays using the numpy array functions

# create array with values and print data type of the array
simple_array = np.array([1, 3, 5])
print (simple_array, simple_array.dtype)

# create an array of ones
ones = np.ones((10, 2))
print(ones.dtype)
print(ones.astype(int))

# create an array of zeros 
zeros = np.zeros((10, 2))
print(zeros)
print(zeros.dtype)
print(zeros.astype(int))

# creating an array within a range of values
range_array = np.arange(0, 10, 2)
print(range_array)

# random array 
random_array = np.random.randint(10, size=(5, 3))
print(random_array)

# Practially goes on and on with different types of arrays you can create with numpy.

# set random seed to 0
# what this basically does it makes sure that the random numbers are generated every time you run the code and set a certain seed 
# which seems useful for different applications and use cases.
np.random.seed(0)
np.random.randint(11, size=(5, 3))

# 3.) viewing arrays and matricies 

a3[:2, :2, :2]
a4 = np.random.randint(10, size=(2, 3, 4))
print(a4.shape)

# 4.) manipulating and comparing arrays 

# Notes

# Basic arithmetic operators -> +, -, *, /, **
# np.exp() exponent function
# np.log() Log function
# Dot product -> np.dot()
# broadcasting 

# Aggregation -> sum, min, max, mean, std, var, argmin, argmax,

# Reshaping 
# reshape() 

# Transpose 
# a3.t

# comparison operators -> ==, !=, >, <, >=, <=




# Broadcasting -> in order  to broadcast, the arrays must have the same size of the trailing axes for both
# arrays in an operation 

 
print(a1, a1.shape)


print(a2.shape)
print(a2 + 2)

# Divide array -> a1 / ones

# Divide using floor division
print (a2 // a1)

# Exponentiation power rule
print (a1 ** 2)

# Square root
np.square(a1)

# Modulus division
print (a1 % a2)

# Logarithm
print(np.log(a1))

# Exponential
print(np.exp(a1))

# Aggregation
print(np.sum(a1))
import random 
massive_list = [random.randint(0, 10) for i in range (100000)]
print (len(massive_list), type(massive_list))
print (massive_list[:10])

start_time = time.time()

np.sum(massive_list)

end_time = time.time()

total_time = end_time - start_time
print(f"Numpy sum took: {total_time:.5f} seconds")
# ---------------------------------------------------------



np.random.seed(0)
matrix = np.random.random(size=(5, 3, 3))
print(matrix)