import pandas as pd

# This library just helps with splitting up the data set
from sklearn.model_selection import train_test_split
# Classification model import library 
from sklearn.ensemble import RandomForestClassifier


# Preparing data through csv file or creating a table manually
heart_disease = pd.read_csv("https://raw.githubusercontent.com/mrdbourke/zero-to-mastery-ml/master/data/heart-disease.csv")
print(heart_disease.head())

# Creating x value for our model
X = heart_disease.drop("target", axis=1)

# Y value for our model
Y = heart_disease["target"]

print(X.head())

print(Y.head(), Y.value_counts())


# Splitting the data into training and test sets (in simple terms training is studying and test is exam which will be the final set)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


# Current hyperparams settings
clf = RandomForestClassifier()
print(clf.get_params())
