#Reading CSV in pandas
import pandas as pd

print("#Read and Print csv")
df = pd.read_csv("files/data.csv")
print(df)
print("#Read and Print csv to string")
print(df.to_string())
