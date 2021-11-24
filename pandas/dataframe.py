#What is dataframe
#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print("#printing a dataframe")
print(df)

#Pandas use the loc attribute to return one or more specified row(s)

print("#printing specific index data from dataframe")
print(df.loc[0])
print(df.loc[[0,2]])

#With the index argument, you can name your own indexes.

df = pd.DataFrame(data,index=["day1","day2","day3"])
print("#printing named index in dataframe")
print(df)


