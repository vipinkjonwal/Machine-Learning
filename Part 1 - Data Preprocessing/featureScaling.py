# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:40:05 2018

@author: Vipin Kumar
"""

# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing Datasets
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[: ,: -1].values
Y = dataset.iloc[: , -1].values

# Handling missing values
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

# Fit the data matrix/values.
imputer = imputer.fit(X[: , 1:3])
X[:, 1:3] = imputer.transform(X[: , 1:3])

# Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelEncoder_X = LabelEncoder()
X[: ,0] = labelEncoder_X.fit_transform(X[: ,0])

oneHotEncoder = OneHotEncoder(categorical_features = [0])
X = oneHotEncoder.fit_transform(X).toarray()

labelEncoder_Y = LabelEncoder()
Y = labelEncoder_Y.fit_transform(Y)

# Splitting the Dataset

from sklearn.cross_validation import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y ,test_size = 0.2, random_state = 0)

# Feature Scaling

from sklearn.preprocessing import StandardScaler

# StandardScaler is a class for feature scaling the variables.

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


