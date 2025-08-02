import numpy as np
# userInput=input("Enter your array input:")
# arr=np.array([int (i)for i in userInput.split()])
# print(arr)

# n=input()

# arr=np.array(list(map(int,input().split())))

# print(arr)



n = int(input()) 
tokens = input().split() 

arr = np.array([int(x) for x in tokens[:n]])  

print(arr)