import numpy
import pandas
import matplotlib
import openpyxl

"""
Author: Muhammad Salman, 100995527
-This file will load in the dataset spreadsheets from kaggle
-It will then proceed to remove all instances of N/A data
-Finally, it will merge all data based on common features
"""

#Load all excel files in through pandas
train  = pandas.read_csv("train.csv")
features = pandas.read_csv("features.csv")
stores  = pandas.read_csv("stores.csv")

#Some values maybe NA depending on stores
#Clean up data

#For unavaialble markdowns, fill with 0
features['Markdown1'] = features["MarkDown1"].fillna(0)
features['Markdown2'] = features['MarkDown2'].fillna(0)
features['Markdown3'] = features['MarkDown3'].fillna(0)
features['Markdown4'] = features['MarkDown4'].fillna(0)
features['Markdown5'] = features['MarkDown5'].fillna(0)

#Remove repeated MarkDown columns
features=features.drop(["MarkDown1", "MarkDown2", "MarkDown3", "MarkDown4", "MarkDown5"], axis=1)

#For unavaialble CPI and Unemployment, take average
meanCPI = features['CPI'].mean()
meanUempl = features['Unemployment'].mean()

features['CPI'] = features['CPI'].fillna(meanCPI)
features['Unemployment'] = features['Unemployment'].fillna(meanUempl)

#Merge data into a single excel file/datafile
main = train.merge(stores, on = 'Store', how = 'left')
main = main.merge(features, on = ['Store', 'Date'], how = 'left')

#IsHoliday will get repeated due to merging data, remove columns
main['IsHoliday'] = main['IsHoliday_y']
main=main.drop(["IsHoliday_y", "IsHoliday_x"], axis=1)
main['IsHoliday'] = main['IsHoliday'].apply(lambda x: 1 if x == 1 else 0)

#Sort date into finer detail
main['Date'] = pandas.to_datetime(main['Date'])
main['Week'] = main['Date'].dt.isocalendar().week
main['Year'] = main['Date'].dt.isocalendar().year
main['Day'] = main['Date'].dt.isocalendar().day
#main['Days-Chrtms'] = 359 - int(main['Date'])
main=main.drop(["Date"], axis=1)

#Transform Type ABC into 1,2,3, respectively
main['Type'] = main['Type'].apply(lambda x: 1 if x == 'A' else(2 if x == 'B' else 3))

#This is will save the new spreadsheet so we can continue analysis
main.to_csv('main.csv')