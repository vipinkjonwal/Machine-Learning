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