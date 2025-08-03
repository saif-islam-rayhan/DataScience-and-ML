import pandas as pd

data = {
    'ID': [1, 2, 3],
    'Name': ['Amina', 'Rahim', 'Shila'],
    'Department': ['CSE', 'EEE', 'BBA'],
    'CGPA': [3.85, 3.50, 3.95],
}

df = pd.DataFrame(data)

# Save Excel file in the target folder
df.to_excel('/home/rayhan/Desktop/DataScience and ML/Pandas/ReadingWritingFile/ExcelFile/myfile.xlsx', index=False)
