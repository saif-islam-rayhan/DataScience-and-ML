import pandas as pd

url = "https://raw.githubusercontent.com/rashakil-ds/5-Minutes-to-Pandas/refs/heads/main/Datasets/bike.csv"
data = pd.read_csv(url)
print(data.head())
