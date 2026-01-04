import numpy as np

x = [i for i in range(1,81) if i%4 == 0]
x = np.array(x)
x = x.reshape(4,5)
print(x)

# Slicing in X...

y = x[0:3,0:3]
print(y)

cop = y.copy()
cop[0,2] = 7
print(cop) 

