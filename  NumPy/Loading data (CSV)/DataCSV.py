import numpy as np

data = np.loadtxt('/home/rayhan/Desktop/DataScience and ML/ NumPy/Loading data (CSV)/data.csv', delimiter=',')
print("Loaded data shape:", data.shape)
print("Data preview:\n", data[:5]) 


#Basic Data Exploration

print("Shape of data:", data.shape)  
print("First row:", data[0])          
print("Mean per column:", data.mean(axis=0))
print("Max per column:", data.max(axis=0))
print("Min per column:", data.min(axis=0))
