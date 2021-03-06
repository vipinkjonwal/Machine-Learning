# Data Preprocessing

# Importing Datasets
dataset = read.csv('Data.csv')

# Handling Missing Values
dataset$Age = ifelse(is.na(dataset$Age), 
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary), 
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)

# Encoding Categorical Data

dataset$Country = factor(dataset$Country,
                         levels = c('France','Spain','Germany'),
                         labels = c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,
                           levels = c('No','Yes'),
                           labels = c(0, 1))

# Splitting the Dataset into Training and Test Set
library(caTools)

set.seed(123)
# set.seed(...) is used to get same results after every execution.

# Splitting for 'TRAINING SET'
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
# sample.split takes argument as Y (Depedent Variable) and Split Ratio for trainig set.

training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)
# Since, training_set is a subset of dataset, we used subset(...).



