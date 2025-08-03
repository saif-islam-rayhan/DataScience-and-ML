import json


data = {
    "students": [
        {"id": 1, "name": "Amina", "department": "CSE", "cgpa": 3.85},
        {"id": 2, "name": "Rahim", "department": "EEE", "cgpa": 3.50},
        {"id": 3, "name": "Shila", "department": "BBA", "cgpa": 3.95}
    ]
}

file_path = '/home/rayhan/Desktop/DataScience and ML/Pandas/ReadingWritingFile/ExcelFile/data.json'

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("JSON file created successfully.")
