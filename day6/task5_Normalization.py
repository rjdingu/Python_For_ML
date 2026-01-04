import numpy as np

arun = [[43,65],[56,87],[68,83]]
arun = np.array(arun)

col_mean  = arun.mean(axis = 0)
print(col_mean)

col_std = arun.std(axis=0)
print(col_std)

arun_norm = (arun - col_mean)/col_std
arun_norm = np.array(arun_norm)

norm_mean = arun_norm.mean(axis=0)
norm_std = arun_norm.std(axis=0)


print(norm_mean)
print(norm_std)