import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NY', 'LA', 'Chicago', 'Miami']
}

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
# print(df)

# Select row with index label 'b'
# print(df.loc['b'])

# Select multiple rows
# print(df.loc[['a', 'c']])

# Select specific column for a row
# print(df.loc['a', 'City'])  # Output: 'NY'

# # Slice using labels
# print(df.loc['b':'d', ['Name', 'Age']])

# Select first row (position 0)
# print(df.iloc[0])

# Select last row
# print(df.iloc[-1])

# # Select multiple rows
# print(df.iloc[[0, 2]])  # First and third rows

# # Select specific value (row 1, column 2)
# print(df.iloc[1, 2])  # Output: 'LA'

# # Slice using positions
# print(df.iloc[1:3, 0:2])  # Rows 1-2, columns 0-1