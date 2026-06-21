import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
# Heart Disease dataset 
heart_disease = pd.read_csv("https://raw.githubusercontent.com/mrdbourke/zero-to-mastery-ml/master/data/heart-disease.csv")
print(heart_disease.head())

# Splitting the data into features through X and Y labels 
X = heart_disease.drop('target', axis=1)
print(X)
y = heart_disease['target']
print(y)

# Declaring the shapes for this dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2)
print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)
# Spliting data 
print(X.shape[0] * 0.8)
print(X.shape[0] * 0.2)



car_sales = pd.read_csv("https://raw.githubusercontent.com/mrdbourke/zero-to-mastery-ml/master/data/car-sales-extended.csv")
print(car_sales)