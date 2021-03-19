import numpy
import pandas
from matplotlib import pyplot as plt
import openpyxl
import seaborn
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
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


#Using Decision Tree Regressor
#y values represent weekly sales, while x contains a series of independant variables
dtree_test = DecisionTreeRegressor(random_state=0)

#Fit training values to generate model
dtree_test.fit(x_train,weekly_sales_train)

#Predict weekly_sales based off sample random test data
#Ideally should be a straight line
predicted_sales = dtree_test.predict(x_test)
print("Score: " +str(dtree_test.score(x_test, weekly_sales_test)))
print("MAE: " + str(mean_absolute_error(weekly_sales_test, predicted_sales)))
print("MSE: " +str(mean_squared_error(weekly_sales_test, predicted_sales)))
print("RMSE: " + str(numpy.sqrt(mean_squared_error(weekly_sales_test, predicted_sales))))

#plt.scatter(weekly_sales_test, predicted_sales)
#ax.set(xlabel='Weekly Sales From Data', ylabel='Predicted Sales')
ax=seaborn.scatterplot(weekly_sales_test, predicted_sales)
ax.set(xlabel='Weekly Sales From Data', ylabel='Predicted Sales')
plt.grid()
plt.show()

