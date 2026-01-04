import numpy as np

arr = [i for i in range (1,13)]
arr = np.array(arr)
print(arr)

# Reshape ...

arr1 = arr.reshape(3,4)
print(arr1)

arr2 = arr.reshape(4,3)
print(arr2)
print(arr2.dtype)

arr3 = arr.flatten()
print(arr3)