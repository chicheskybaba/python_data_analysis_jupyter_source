# import the libraries

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd


# Next, download the iris dataset from its weblink as follows


path = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"


# Next, we need to assign column names to the dataset as follows

headernames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']


# Now, we need to read dataset to pandas dataframe as follows

dataset = pd.read_csv(path, names=headernames)


# print the top part of the dataset

print (dataset.head())



# Data Preprocessing will be done with the help of following script lines

X = dataset.iloc[:, :-1].values

y = dataset.iloc[:, 4].values



# Next, we will divide the data into train and test split. The following code will split the dataset into 70% training data and 30% of testing data

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)



# Next, train the model with the help of RandomForestClassifier class of sklearn as follows

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=50)

classifier.fit(X_train, y_train)



# At last, we need to make prediction. It can be done with the help of following script

y_pred = classifier.predict(X_test)



# Next, print the results as follows


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

result = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")

print(result)

result1 = classification_report(y_test, y_pred)

print("Classification Report:",)

print (result1)

result2 = accuracy_score(y_test,y_pred)

print("Accuracy:",result2)












