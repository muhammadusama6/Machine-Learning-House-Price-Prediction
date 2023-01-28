# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ARzZcqA0b9WsavUbaspwEAzPoSCh1M8M
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('housing.csv')

data.info()

data.dropna(inplace = True)

data.info()

from sklearn.model_selection import train_test_split

x = data.drop(['median_house_value'], axis = 1)
y = data['median_house_value']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

train_data = x_train.join(y_train)

train_data.hist(figsize = (15, 8))



plt.figure(figsize = (15,8))
sns.heatmap(train_data.corr(), annot = True, cmap = 'YlGnBu')

train_data['total_rooms'] = np.log(train_data['total_rooms'] + 1)
train_data['total_bedrooms'] = np.log(train_data['total_bedrooms'] + 1)
train_data['population'] = np.log(train_data['population'] + 1)
train_data['households'] = np.log(train_data['households'] + 1)

train_data.hist(figsize = (15, 8))

train_data .ocean_proximity.value_counts()

train_data = train_data.join(pd.get_dummies(train_data.ocean_proximity))

train_data = train_data.drop(['ocean_proximity'], axis = 1)
train_data

plt.figure(figsize = (15,8))
sns.heatmap(train_data.corr(), annot = True, cmap = 'YlGnBu')

from sklearn.linear_model import LinearRegression

x_train, y_train = train_data.drop(['median_house_value'], axis = 1), train_data['median_house_value']

reg = LinearRegression()
reg.fit(x_train, y_train)

test_data = x_test.join(y_test)

test_data['total_rooms'] = np.log(test_data['total_rooms'] + 1)
test_data['total_bedrooms'] = np.log(test_data['total_bedrooms'] + 1)
test_data['population'] = np.log(test_data['population'] + 1)
test_data['households'] = np.log(test_data['households'] + 1)

test_data = test_data.join(pd.get_dummies(test_data.ocean_proximity))
test_data = test_data.drop(['ocean_proximity'], axis = 1)

x_test, y_test = test_data.drop(['median_house_value'], axis = 1), test_data['median_house_value']

#I did a mistake, somehow ISLAND was not showing in x_test. 
#So, there was difference between no. of columns of x_train and x_test
#That's why I added ISLAND column into x_test manually
#Placed zeros because out of total 20000 entries, only 5 ISLANDS
#ISLAND has not significant effect on our model
x_test.insert(loc=x_test.columns.get_loc("INLAND") + 1, column="ISLAND", value=0)

reg.score(x_test, y_test)