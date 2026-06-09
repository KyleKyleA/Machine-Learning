import numpy as np
import pandas as pd
# Two rules for dot product:
# 1.) inner dimensions must match 
# 2.) the resulting matrix has the shape of the outer dimension 

# Example 1
# Declare random seed
np.random.seed(0)

# Declare matrices 
mat1 = np.random.randint(10, size=(3, 3))
mat2 = np.random.randint(10, size=(3, 2))

# Print result 
print(mat1.shape, mat2.shape)


print(mat1)
print(mat2)

print(np.dot(mat1, mat2))
print(mat1 @ mat2)
# -----------------------------------------------
#Example 2
np.random.seed(0)
mat3 = np.random.randint(10, size=(4, 3))
mat4 = np.random.randint(10, size=(4, 3))
print(mat3)
print(mat4)
print(mat3.T.shape)

# How to print a dot product 
print(np.dot(mat3.T, mat4))

# Elemental wise multiplying 
print(mat3 * mat4)


# ---------------------------------------------
# practical example
np.random.seed(0)
sales_amts = np.random.randint(20, size=(5, 3))
print(sales_amts)

# Implementing table using table size 
# Index 
# and columns with values 
weekly_sales = pd.DataFrame(sales_amts, 
                            index=["Mon", "Tues", "Weds", "Thurs", "Fri"],
                            columns=["Almond Butter", "Peanut Butter", "Cashew Butter"])

print(weekly_sales)   

prices = np.array([10, 8, 12])
print(prices)      

# Now doing butter prices 
# Reshaping
butter_prices = pd.DataFrame(prices.reshape(1, 3),
                             index=["Price"],
                             columns=["Almond Butter", "Peanut Butter", "Cashew Butter"])  
print(butter_prices.shape)   
print(weekly_sales.shape)

# Find total amount of sales for a whole day
# total_sales = prices.dot(sales_amts)
# print(total_sales)

# result in valueError meaning it's doesn't match
print(prices)
print(sales_amts.T.shape)

# A way to fix the value error would have to be transposing 
total_sales = prices.dot(sales_amts.T)
print(total_sales)

print(butter_prices.shape, weekly_sales.shape)

# Daily sales
daily_sales = butter_prices.dot(weekly_sales.T)
print(daily_sales)
weekly_sales["total"] = daily_sales.T
print(weekly_sales)