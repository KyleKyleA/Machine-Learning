import pandas as pd
import numpy as np
# This library just helps with splitting up the data set
from sklearn.model_selection import train_test_split
# Classification model import library 
from sklearn.ensemble import RandomForestClassifier
# Metrics import
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

# Saving model
import pickle

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

# Fitting the model into the dataset
print(clf.fit(X=X_train, y=y_train))

# Prediction by using the model we are using
# ValueError
# y_label = clf.predict(np.array([0,2,3,4])) The terminal sees it as a 1d array instead of a 2d array

print(X_test.head())
y_preds = clf.predict(X=X_test)

# evaluating the model on the training set
train_acc = clf.score(X=X_train, y=y_train)
print(f"The model's accuracy on the training set is: {train_acc*100}%")

# Evaluating model on the test set
test_acc = clf.score(X=X_test, y=y_test)
print(f"The model's accuracy on the testing dataset is: {test_acc*100:.2f}%")

# Creating a classification report
print(classification_report(y_test, y_preds))
print(accuracy_score(y_test, y_preds))

# trying different numbers of estimators 
np.random.seed(42)
for i in range(100, 200, 10):
    print(f"Trying model with {i} estimators...")
    model = RandomForestClassifier(n_estimators=i).fit(X_train, y_train)
    
    model_score = model.score(X_test, y_test)
    print(f"The model's accuracy on the testing dataset is: {model.score(X_test, y_test):.2f}%")
    
    # Measure validation score across different sets and spilts either from test or train
    cross_val_mean = np.mean(cross_val_score(model, X, Y, cv=5))
    print(f"5-fold cross-validation score: {cross_val_mean * 100:.2f}")
    print("")


# Grid search
np.random.seed(42)

# Define the parameters to search over in the dictionary form
param_grid = {'n_estimators': [i for i in range(100, 200, 10)]}
# setup grid search 
grid = GridSearchCV(estimator=RandomForestClassifier(),
                    param_grid=param_grid,
                    cv=5,
                    verbose=1)
# Fit the grid search into the data
grid.fit(X, Y)
print(f"The best parameter values are: {grid.best_params_}")
print(f"With a score of: {grid.best_score_*100:.2f}%")

# setting 
clf = grid.best_estimator_
print(clf) 

# fit the best model
clf = clf.fit(X_train, y_train)
print(f"Best model score on a single split of the data:  {clf.score(X_test, y_test)*100:.2f}%")


# Saving model 
pickle.dump(model, open("random_forest_model_1.pkl", "wb"))

# loading model
loaded_pickle_model = pickle.load(open("random_forest_model_1.pkl", "rb"))
print(f"Loaded pickle model prediction score: {loaded_pickle_model.score(X_test, y_test) * 100:.2f}%")