import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NY', 'LA', 'Chicago', 'Miami']
}

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
# print(df)
# People older than 30
print(df[df['Age'] > 30])

# # Multiple conditions
print(df[(df['Age'] > 25) & (df['City'] == 'LA')])

# # Using isin()
print(df[df['City'].isin(['NY', 'Chicago'])])