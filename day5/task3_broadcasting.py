import numpy as np

arr = [i for i in range(1,10)]
arr = np.array(arr)
arr1 = arr.reshape(3,3)


arr2 = np.array([1,2,3])

print(arr1.shape)
print(arr2.shape)
arr2 = arr2.reshape(3,1)

print(arr1 + arr2)


# Subtract Column wise Mean with Original array
arrNew = [i for i in range(1,45) if i % 5 == 0]
arrNew = np.array(arrNew)
arrNew = arrNew.reshape(4,2)


arr_col = np.array(arrNew.mean(axis = 0))
print(arr_col.shape)

arr_col = arr_col.reshape(4,1)

print (arrNew - arr_col)