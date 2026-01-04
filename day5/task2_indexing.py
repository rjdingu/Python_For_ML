import numpy as np
arr = [i for i in range(1,10)]

arr = np.array(arr) # Here the list is converted into array
arr3 = arr.reshape(3,3) # Reshape


# First 2 rows
print(arr3[0:2,:3])

# First 2 columns 
print(arr3[:,0:2])

# Centre 
print(arr3[1:2,:])

# Diagonal
print(arr3.diagonal())

# Center element 
dia = arr3.diagonal()
print(dia[1])


# Aray * 5 and square the element

print(arr * 5)
print(arr * arr)

# SUM
# Using .sum()

print(arr3.sum())   # Output = 45

# Using loop 
s = 0
for i in arr3:
    s = s + i
print(s)    # Output = [12 15 18]   where 12+15+18 = 45

