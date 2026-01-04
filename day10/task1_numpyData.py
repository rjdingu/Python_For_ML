import pandas as pd
import numpy as np
data = pd.read_csv("D:\PythonProgramming\prepML\day10\marksheet.csv")
print(data)
print(data.describe())


# Normalization
tm = data['Total_Mark(%)']
tm_mean = data['Total_Mark(%)'].mean(axis = 0)
tm_std = data['Total_Mark(%)'].std(axis = 0)

tm_norm = (tm - tm_mean)/tm_std

arr_tmNorm = np.array(tm_norm)
arr_tmNorm.reshape(5,5)
print(arr_tmNorm)

norm_mean = tm_norm.mean()
norm_std = tm_norm.std()
print('\n Normalization Mean(0) : \n')
print(norm_mean)

print('\n Normalization STD(1) :')
print(norm_std)


