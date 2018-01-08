# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 20:44:22 2018

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
# sklearn has libraries to make machine learning models.
# preprocessing sub-library contains classes, methods to preprocess.
# From this library, we're importing Imputer class, which will allow us to 
# take care of missing data.

# Creating an object of class Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)

# Fit the data matrix/values.
imputer = imputer.fit(X[: , 1:3])
X[:, 1:3] = imputer.transform(X[: , 1:3])

