import pandas 
import numpy as np

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# myvar = pandas.DataFrame(mydataset)
# print(myvar)


import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# myvar = pd.DataFrame(mydataset)
# print(myvar)

# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.
# a = [1, 7, 2]
# myvar = pandas.Series(a)
# print(myvar)
# This label can be used to access a specified value.
# print(myvar[0])

# With the index argument, you can name your own labels.
# a = [1, 7, 2]
# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)

# When you have created labels, you can access an item by referring to the label.
# print(myvar["y"])

# Create a simple Pandas Series from a dictionary:
# The keys of the dictionary become the labels.
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
# print(myvar)

# Create a Series using only data from "day1" and "day2":
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories, index = ["day1", "day2"])
# print(myvar)

# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# myvar = pd.DataFrame(data)
# print(myvar)


# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# myvar = pd.DataFrame(data)
# print(myvar)
# # Pandas use the loc attribute to return one or more specified row(s)
# print(myvar.loc[[0,1]])


# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# myvar = pd.DataFrame(data)
# print(myvar)
# # Pandas use the loc attribute to return one or more specified row(s)
# print(myvar.loc[0])


# Give your own index values
# data = {
#   "calories": [420, 380,6],
#   "duration": [50, 40, 45]
# }
# myvar = pd.DataFrame(data,index=["day1","day2","day3"])
# print(myvar)
# # Pandas use the loc attribute to return one or more specified row(s)
# print(myvar.loc[["day1","day2"]])

# If your data sets are stored in a file, Pandas can load them into a DataFrame.
# df = pd.read_csv('data.csv')
# print(df) 

#Tip: use to_string() to print the entire DataFrame.
#df = pd.read_csv('data.csv')
# print(df.to_string()) 


#Check the number of maximum returned rows:
#print(pd.options.display.max_rows) 


#Increase the maximum number of rows to display the entire DataFrame:
# pd.options.display.max_rows = 9999
# df = pd.read_csv('data.csv')
# print(df) 



