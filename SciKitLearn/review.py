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
##############################################################################

# Car sales dataset 
from sklearn.ensemble import RandomForestClassifier

# Theses two libraries help convert string values from a table into a numerical since machine learning prefers that
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


car_sales = pd.read_csv("https://raw.githubusercontent.com/mrdbourke/zero-to-mastery-ml/master/data/car-sales-extended.csv")
print(car_sales)
print(car_sales.dtypes)

categorical_features = ["Make", "Colour", "Doors"] 

X = car_sales.drop("Price", axis=1)
y = car_sales['Price']
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2)

one_hot = OneHotEncoder()

# creating an instance for the transformer 
transformer = ColumnTransformer([("one_hot",
                                  one_hot,
                                  categorical_features,
                                  )],
                                remainder="passthrough")

# turn the features that were valued string into numerical values that will return into byte matrices codes
transformed_X = transformer.fit_transform(X)
print(transformed_X)

print(X.head())

# Example of printing the index of 0 into transformed integer values that can get crazy
print(transformed_X[0])



# Splitting the data below



# model = RandomForestRegressor()
# model.fit(X_train, Y_train)
# model.score(X_test, Y_test)


