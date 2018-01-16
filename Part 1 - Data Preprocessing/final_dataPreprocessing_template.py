# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:17:32 2018

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

# Splitting the Dataset

from sklearn.cross_validation import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y ,test_size = 0.2, random_state = 0)

'''
# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''



