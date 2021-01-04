import pandas as pd
df = pd.read_csv("data/vehicles.csv")
print("The shape of the dataframe is", df.shape)
print("It has a total of", len(df), "rows")
print("it has a total of", len(df.columns), "columns")
