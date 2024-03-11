import pandas as pd
# Get a quick overview by printing the first 10 rows of the DataFrame:
# df = pd.read_csv('data.csv')
# print(df.head(10))



#if the number of rows is not specified, the head() method will return the top 5 rows.
#df = pd.read_csv('data.csv')
# print(df.head())
#Print the last 5 rows of the DataFrame:
#print(df.tail()) 
#Print information about the data:
#print(df.info()) 


# df = pd.read_csv('data.csv')
# Return a new Data Frame with no empty cells:
# new_df = df.dropna()
# print(new_df.to_string())


# Remove all rows with NULL values:
# df = pd.read_csv('data.csv')
# #Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.
# df.dropna(inplace = True)

# print(df.to_string())


# # The fillna() method allows us to replace empty cells with a value:
# df = pd.read_csv('data.csv')
# #Replace NULL values with the number 130:
# df.fillna(130, inplace = True)


#Calculate the MEAN, and replace any empty values with it:
# df = pd.read_csv('data.csv')
# df["Calories"].fillna(130, inplace = True)
# print(df.to_string())



# One way to fix wrong values is to replace them with something else.
# df = pd.read_csv('data.csv')
# #Set "Duration" = 600 in row 7:
# df.loc[7, 'Duration'] = 600
# print(df.to_string())




#Loop through all values in the "Duration" column.
#If the value is higher than 120, set it to 120:
# df = pd.read_csv('data.csv')
# for x in df.index:
#   if df.loc[x, "Duration"] >= 70:
#     df.loc[x, "Duration"] = 0
#     print(df.to_string())



# Delete rows where "Duration" is higher than 30:
# df = pd.read_csv('data.csv')
# for x in df.index:
#   if df.loc[x, "Duration"] > 20:
#     df.drop(x, inplace = True)
# print(df.to_string())



#Returns True for every row that is a duplicate, otherwise False:
# df = pd.read_csv('data.csv')
# print(df.duplicated())



#To remove duplicates, use the drop_duplicates() method.
#Remove all duplicates:
# df = pd.read_csv('data.csv')
# df.drop_duplicates(inplace = True)
# print(df.to_string())




