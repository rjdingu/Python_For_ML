import pandas as pd
data = pd.read_csv('D:\PythonProgramming\prepML\day4\marksheet.csv')
# Checking any Null value is present in the data
#print(data.isnull().sum())
'''
Filling missing values 

Method 1 : Using ffill or bfill

'''


m1 = data['Gender'].fillna(method = 'ffill',inplace = True)
print(m1)
print(data.isnull().sum())



# Method 2 : Using .mean()

m2 = data['Science'].fillna(data['Science'].mean(),inplace = True)
print(data.isnull().sum())

# Method 3 : Using assingning particular value 

m3 = data['Age'].fillna(15,inplace = True)
print(data.isnull().sum())

# Method 4 Without using inplace 

data['History'] = data['History'].fillna(data['History'].std())
print(data.isnull().sum())

print(data)



