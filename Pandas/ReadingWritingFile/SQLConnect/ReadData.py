import pandas as pd
import pymysql


connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',           
    database='Test_db'
)

# SQL query
query = "SELECT * FROM users;"

# Data read using pandas
df = pd.read_sql(query, connection)

# Print the DataFrame
print(df)

connection.close()
