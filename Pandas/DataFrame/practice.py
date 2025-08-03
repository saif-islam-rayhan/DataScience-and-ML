import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 22],
    "City": ["Dhaka", "Chittagong", "Rajshahi"]
}

df = pd.DataFrame(data)
# print(df)
# Shows 5 rows
print(df.head())
print(df.columns)
print(df.shape)
print(df.describe())
print(pd.DatetimeIndex)