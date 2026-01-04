import numpy as np

arr = [i for i in range(1,21)]
arr = np.array(arr)
# Element divisible by 3...
diviBy3 = arr[ arr % 3 == 0]
print(diviBy3)

# Element greater than 10
gt = arr[ arr >= 10]
print(gt)

# Replaceing number less than 5 with 0
arr[ arr < 5] = 0
print(arr)

# Count the replacing numbers
l = arr[arr<5]
print(len(l))