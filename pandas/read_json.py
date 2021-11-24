#Reading CSV in pandas

import pandas as pd

df = pd.read_json('files/data.json')
print("#Print Head and tail Data")
print(df)
print("#Whole Data")
print(df.to_string())