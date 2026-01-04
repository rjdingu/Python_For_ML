import numpy as np
print(np.__version__)

# Print 1D array
n1 = np.array([0,1,2,3,4,5,6,7,8])
print(n1)

# Reshape n1
n2 = n1.reshape(3,3)
print(n2)

# Print the first two rows
n3 = n2[:2,:]
print(n3)

# Print the last column
n4 = n2[:,-1:]
print(n4)

# Adding two array each element_wise
n5 = np.array([0,12,3,4,5,6,87,9,41])
n5 = n5.reshape(3,3)

n6 = n5 + n2
print(n6)

# Print the Mean of an array
#n7 = np.mean(n6)
#print(n7)

# Add all the Rows
s = np.sum(n6,axis = 1)
print(s)

# Add all the Columns
s = np.sum(n6,axis = 0)
print(s)

# Print Standard deviation all the Columns
std_clm = np.std(n6,axis = 0)
print(std_clm)


# Print Standard deviation all the Rows
std_rw = np.std(n6,axis = 1)
print(std_rw)