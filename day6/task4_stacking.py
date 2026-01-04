import numpy as np

arr1 = [4,57,89,12,68,14,65,54,3]
arr1 = np.array(arr1)
arr1 = arr1.reshape(3,3)
print(arr1.shape)


arr2 = [5,10,45,7,43,76,8,43,9]
arr2 = np.array(arr2)
arr2 = arr2.reshape(3,3)
print(arr2.shape)

# Stacking .. 
result0 = np.stack((arr1,arr2),axis = 0)
print('\nWith axis = 0, \nThe stacking... \n ')
print(result0)

print('\nWith axis = 1, \nThe stacking... \n ')
result1 = np.stack((arr1,arr2),axis = 1)
print(result1)


# Vertical Stacking
print("The original arr1 \n:")
print(arr1)
print("The original arr2 \n:")
print(arr2)
result_vstack = np.vstack((arr1,arr2))
print("\nThe result of vertical Stacking :\n")
print(result_vstack)

print ("The shape of the resulted vvertical stacking:\n")
print(result_vstack.shape)

# Horizontal Stacking
result_hstack = np.hstack((arr1,arr2))

print("\nThe result of Horixontal Stacking :\n")
print(result_hstack)
print ("\nThe shape of the resulted horizontal stacking:\n")
print(result_hstack.shape)


# Concating

result_concat = np.concat((arr1,arr2))
print(result_concat)