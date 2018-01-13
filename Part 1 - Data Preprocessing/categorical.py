# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 14:52:21 2018

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

# Creating an object of class Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

# Fit the data matrix/values.
imputer = imputer.fit(X[: , 1:3])
X[:, 1:3] = imputer.transform(X[: , 1:3])

# Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# LabelEncoder is a class in sklearn.preprocessing library 
# used to encode categorical data without bothering order.

labelEncoder_X = LabelEncoder()
# labelEncoder_X is Object of LabelEncoder class.

X[: ,0] = labelEncoder_X.fit_transform(X[: ,0])
# This will set France to 0, Germany to 1 and Spain to 2 but we should 
# prevent machine learning model to compare beween categorical data.

# To prevent this, we will create dummy variables.
# For this, we'll import a new class 'OneHotEncoder' class.

oneHotEncoder = OneHotEncoder(categorical_features = [0])
# categorical_features specify what features are treated as categorical.

X = oneHotEncoder.fit_transform(X).toarray()
# This will convert the Country Data into dummy paarmeters
# with three columns (as we have three categories of country).

# For the dependent variable, we need not to make dummy parameters
# because machine model knows that it is a category and there's no 
# order between these two.

# Encoding the dependent variable Y which has two categories i.e, Yes and No
labelEncoder_Y = LabelEncoder()
Y = labelEncoder_Y.fit_transform(Y)






