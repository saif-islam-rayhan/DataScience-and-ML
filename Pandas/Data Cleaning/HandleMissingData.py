import pandas as pd
import numpy as np

# Create sample data with missing values
data = {
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Age': [25, np.nan, 35, None, 28],
    'Salary': [50000, 60000, np.nan, None, 45000],
    'Join_Date': ['2020-01-15', '2019-03-22', None, None, '2021-11-05']
}
df = pd.DataFrame(data)

# Display missing values
print("Missing values count:")
print(df.isna().sum())

# # Solution 1: Drop rows with any missing values
clean_df = df.dropna()
print("\nAfter dropping missing rows:")
print(clean_df)

# # Solution 2: Fill missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(0, inplace=True)
df['Name'].fillna('Unknown', inplace=True)
df['Join_Date'].fillna(pd.to_datetime('today').strftime('%Y-%m-%d'), inplace=True)

print("\nAfter filling missing values:")
print(df)