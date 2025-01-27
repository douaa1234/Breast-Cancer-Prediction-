# -*- coding: utf-8 -*-
"""BreastCancerClassifier.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q5WiSuh6dJza4jNQQJL2BjOO-99Xl-4H
"""

#imports
import pandas as pd
import seaborn as sns

import os
os.environ['KAGGLE_USERNAME']='douaa1234'
os.environ['KAGGLE_KEY']='8ef5140fc9562b9a6bc32beb30d7630e'

!kaggle datasets download -d uciml/breast-cancer-wisconsin-data

! unzip /content/breast-cancer-wisconsin-data.zip

#load data on dataframe:a data structure
df = pd.read_csv('/content/data.csv')

#display dataframe
df.head()

df.shape
#rows+columns

df.isna().sum()

#remove unnamed column
df.dropna(axis=1,inplace=True)

df.shape

df['diagnosis'].value_counts()

df.dtypes

#Turn the labels into categorical values
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
df.iloc[:,1] = encoder.fit_transform(df.iloc[:,1].values)

#display df
df

#splitting data into independent and dependent
#independet dataset with all features
X = df.iloc[:,2:].values
Y = df.iloc[:,1].values

#splitting data into trainign an dtesting
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.25)

#standardize the data / feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

X_train

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
Y_train = Y_train.astype(int)
Y_test = Y_test.astype(int)
#classifier.fit(X_train,Y_train)
classifier = LogisticRegression()
classifier.fit(X_train, Y_train)

prediction = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
import seaborn as sns
cm = confusion_matrix(Y_test,prediction)
print(cm)
sns.heatmap(cm,annot=True)

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,prediction))

import pickle

# Assuming `classifier` is your trained LogisticRegression model
with open('logistic_regression_model.pkl', 'wb') as file:
    pickle.dump(classifier, file)

from google.colab import files

# Download the file
files.download('logistic_regression_model.pkl')