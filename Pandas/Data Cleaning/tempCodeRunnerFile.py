df['Salary'].fillna(0, inplace=True)
df['Name'].fillna('Unknown', inplace=True)
df['Join_Date'].fillna(pd.to_datetime('today').strftime('%Y-%m-%d'), inplace=True)
