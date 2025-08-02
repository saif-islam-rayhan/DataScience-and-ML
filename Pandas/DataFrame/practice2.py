import pandas as pd
data= {'name':["saif","safin","sorif"],'Age':[22,44,55]}
df=pd.DataFrame(data)
# # print(df)

# Single column
# ages=df['Age']
# print(ages)

# Multiple columns
# subset=df[['Age','name']]
# print(subset)


# Rows by index
# firstrow=df.iloc[0]
# print(firstrow)

# namedrow=df.loc[0]
# print(namedrow)
print(type(data))
s={3,3,5,6,7,8}
s2=pd.Series(list(s))
print(s2)
print(type(s))
print(s)

l=[3,4,5,6,7,7,8]
se=set(l)
print(se)
