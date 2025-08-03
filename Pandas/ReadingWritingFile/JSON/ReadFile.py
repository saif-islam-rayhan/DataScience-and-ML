import json

file_path = '/home/rayhan/Desktop/DataScience and ML/Pandas/ReadingWritingFile/ExcelFile/data.json'


with open(file_path, 'r') as f:
    data = json.load(f)

print("Data read from JSON:")
print(data)
