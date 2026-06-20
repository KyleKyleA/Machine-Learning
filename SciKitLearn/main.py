import pandas as pd

# Preparing data through csv file or creating a table manually
heart_disease = pd.read_csv("https://raw.githubusercontent.com/mrdbourke/zero-to-mastery-ml/master/data/heart-disease.csv")
print(heart_disease.head())

# Creating x value for our model
X = heart_disease.drop("target", axis=1)

# Y value for our model
Y = heart_disease["target"]

print(X.head())

print(Y.head(), Y.value_counts())

