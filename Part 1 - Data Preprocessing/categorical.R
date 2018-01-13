# Data Preprocessing

# Importing Datasets
dataset = read.csv('Data.csv')

# Handling Missing Values
dataset$Age = ifelse(is.na(dataset$Age), 
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age
                    )

dataset$Salary = ifelse(is.na(dataset$Salary), 
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary
                       )
# is.na is used to check is value in dataset is missing or not.

# Encoding Categorical Data

# To do this, we will use factor() function which transform categorical
# variable into numeric data but in for  of factors.

dataset$Country = factor(dataset$Country,
                         levels = c('France','Spain','Germany'),
                         labels = c(1,2,3)
                        )

dataset$Purchased = factor(dataset$Purchased,
                           levels = c('No','Yes'),
                           labels = c(0, 1)
                          )


