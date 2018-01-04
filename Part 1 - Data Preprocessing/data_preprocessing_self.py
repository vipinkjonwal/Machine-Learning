# Data Preprocessing

# Importing Libraries
import numpy as np
# numpy is used for mathematics which we used in machine learning.

import matplotlib.pyplot as plt
# matplotlib is used for plotting charts and pyplot is sub-library which has 
# intuitive and useful tools for plotting. 

import pandas as pd
# Pandas library is a library used to import data sets and manage data sets.

# Importing Datasets
# First thing to do before import datasets is that we should set and specify
# the working directory where out data sets are contained.

dataset = pd.read_csv('Data.csv')
# read_csv is function in pandas library to read the csv file.

# We need to distinguish the matrix features and the dependent variable
# vector.

X = dataset.iloc[: ,: -1].values
# X is independent variable vector.
# [: , : -1] means we are taking all the rows and for the columns, we are
# excluding last column because it is dependent variable column.
# .values means we are taking all the values.

Y = dataset.iloc[: , -1].values
# Y is dependent variable vector.
# [: , : -1] means we are taking all the rows and for the columns, we are
# taking last column because it is dependent variable column.
# To include last column, we can either write the indexof last column,
# or we can write -1 for it as -1 is index of last column in Python.



