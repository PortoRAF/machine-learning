#Data Preprocessing

#Importing the libraries
import numpy as np #for math
import matplotlib.pyplot as plt #for plotting
import pandas as pd #for dataset handling

#Importing the dataset
dataset = pd.read_csv('Data.csv')
#Creating matrix of features
#[:, :-1] -> Take all lines and all columns except the last one (-1)
X = dataset.iloc[:, :-1].values

#Creating dependant variable vector
#Take all lines and only the last column
Y = dataset.iloc[:, 3].values

#Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy = 'mean', axis = 0)
#Fit features matrix into imputer
#[:, 1:3] -> Take all lines and columns 1 and 2
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#Enconding categorical data
#Replace text columns by numbers so we can include the numbers in the equations
'''
This method of encoding generates a problem as it set numbers with different
"weights" to each entry. This way, the equation will understand that an entry
is greater than the other, when in fact they all should have the same value

from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
'''
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
#OneHotEncoder splits the categorical column in three
#categorical_features=[0] defines only the first column to be transformed
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
#Encode the dependant variable
labelencoder_y = LabelEncoder()
Y = labelencoder_y.fit_transform(Y)