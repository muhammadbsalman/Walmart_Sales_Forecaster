import numpy
import pandas
from matplotlib import pyplot as plt
import openpyxl
import seaborn

"""
Author: Muhammad Salman, 100995527

"""

#Load all excel files in through pandas
main  = pandas.read_csv("main.csv")
train  = pandas.read_csv("train.csv")
features = pandas.read_csv("features.csv")
stores  = pandas.read_csv("stores.csv")
"""
#Each store has a type (A,B,C) with an associated size
#Find type of store and its size
type_store = []
size_store = []

row =0
while row<len(stores.index):
    type_store.append(stores.at[row,'Type'])
    size_store.append(stores.at[row,'Size'])
    row+=1

#Plot Graph
plt.title('Store Classification')
plt.xlabel('Store Type')
plt.ylabel('Store Size')
plt.scatter((type_store), (size_store))
plt.show()

#Correlation between Store Type and Sales
sales_store = []
sales_store = pandas.concat([main['Type'], main['Weekly_Sales']], axis=1)
seaborn.scatterplot(data=sales_store, x = "Type", y = "Weekly_Sales")
plt.show()

#Correlation between if it is a Holiday vs. Sales
holiday_store = []
holiday_store = pandas.concat([(main['IsHoliday']), main['Weekly_Sales']], axis=1)

fig, ax = plt.subplots()
seaborn.barplot(data=holiday_store, x = "IsHoliday", y = "Weekly_Sales")
#ax.set_xlim(0,1)
#ax.set_xticks([0,1])
plt.show()
"""
"""
#Correlation between Week and Weekly_Sales
sale_week = main.groupby(['Week']).agg({'Weekly_Sales': ['mean']})
ax=seaborn.barplot(sale_week['Weekly_Sales']['mean'].index, sale_week['Weekly_Sales']['mean'].values)
plt.grid()
ax.set(xlabel='Week', ylabel='Sales')
plt.xticks(range(1, 53, 1))
plt.show()
"""
"""
#Correlation between Dept and Weekly_Sales
sale_department = main.groupby(['Dept']).agg({'Weekly_Sales': ['mean']})
ax=seaborn.barplot(sale_department['Weekly_Sales']['mean'].index, sale_department['Weekly_Sales']['mean'].values)
plt.grid()
ax.set(xlabel='Department', ylabel='Sales')
plt.xticks(range(1, len(sale_department), 1))
plt.show()
"""
"""
#Correlation between Store and Weekly_Sales
sale_store = main.groupby(['Store']).agg({'Weekly_Sales': ['mean']})
ax=seaborn.barplot(sale_store['Weekly_Sales']['mean'].index, sale_store['Weekly_Sales']['mean'].values)
plt.grid()
ax.set(xlabel='Store', ylabel='Sales')
plt.xticks(range(1, len(sale_store), 1))
plt.show()
"""