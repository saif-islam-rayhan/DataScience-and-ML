import pandas as pd


data = pd.Series([10, 20, 30, 40, 50])
print(data)

data1=pd.Series([3,4,5,6],index=['a','b','c','d'])
print(data1)
print(data1.values)
print(data1.index)
print(data1.iloc[0])
print(data1.loc['b'])