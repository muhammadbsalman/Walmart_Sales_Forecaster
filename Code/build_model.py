import numpy
import pandas
from matplotlib import pyplot as plt
import openpyxl
import seaborn

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

"""
Author: Muhammad Salman, 100995527

"""

#Load all excel files in through pandas
main  = pandas.read_csv("main.csv")
train  = pandas.read_csv("train.csv")
features = pandas.read_csv("features.csv")
stores  = pandas.read_csv("stores.csv")

weekly_sales_train = main['Weekly_Sales']
x_train = main.drop(['Weekly_Sales'], axis=1)
x_train = x_train.drop(['Unnamed: 0'], axis=1)

#Split data into train/test, let test be 20% of total data imported from main dataframe
x_train,x_test,weekly_sales_train,weekly_sales_test=train_test_split( x_train, weekly_sales_train, test_size=0.20, random_state=0)


#Using KNN Regression Model
#y values represent weekly sales, while x contains a series of independant variables
knn_test = KNeighborsRegressor(n_neighbors=15, n_jobs=4)

#Fit training values to generate model
knn_test.fit(x_train,weekly_sales_train)

#Predict weekly_sales based off sample random test data
#Ideally should be a straight line
predicted_sales = knn_test.predict(x_test)
print(knn_test.score(x_test, weekly_sales_test))

#plt.scatter(weekly_sales_test, predicted_sales)
#ax.set(xlabel='Weekly Sales From Data', ylabel='Predicted Sales')
ax=seaborn.scatterplot(weekly_sales_test, predicted_sales)
ax.set(xlabel='Weekly Sales From Data', ylabel='Predicted Sales')
plt.grid()
plt.show()

