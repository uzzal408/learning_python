#A pandas series like a column in a table
#It is one dymentional array holding data of any type

import pandas as pd

a = [1, 7, 2]
myvar = pd.Series(a)
print('Printing a Series')
print(myvar)

#Lebel, If nothing else is specified, the values are labeled with their index number.
#This label can be used to access a specified value.

print(myvar[1])

#Create Lebel

createLb = pd.Series(a,index=["x","y","z"])
print('Printing a Series With Label')
print(createLb)
print('Printing a specific label from series')
print(createLb["z"])

#Key/Value Objects as Series

calories = {"day1": 420, "day2": 380, "day3": 390}
keyValueSeries = pd.Series(calories)
print('Printing a Key/Value Type Serice')
print(keyValueSeries)

#To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
selectSomeFromSeries = pd.Series(calories,index=["day1","day2"])
print('Printing a some selective data from series')
print(selectSomeFromSeries)

#DataFrames
#Data sets in Pandas are usually multi-dimensional tables, called DataFrame
#Series is like a column, a DataFrame is the whole table.

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print("Printing a Dataframe")
print(df)