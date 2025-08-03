import pandas as pd

file_path = '/home/rayhan/Desktop/DataScience and ML/Pandas/ReadingWritingFile/ExcelFile/myfile.xlsx'


df = pd.read_excel(file_path, engine='openpyxl')


print(df)