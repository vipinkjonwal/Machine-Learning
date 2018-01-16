# Data Preprocessing

# Importing Datasets
dataset = read.csv('Data.csv')
# dataset = dataset[, 2:3]

# Splitting the Dataset into Training and Test Set
library(caTools)

set.seed(123)

# Splitting for 'TRAINING SET'
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])





