import pandas as pd
ds = pd.read_csv('D:\PythonProgramming\prepML\day9\marksheet.csv')

ds = ds.fillna(method = 'ffill')

'''ds['History'] = ds['History'].fillna(method = 'ffill')
ds['Science'] = ds["Science"].fillna(method = 'bfill')
ds['Age'] = ds['Age'].fillna(method  = 'bfill')
ds['Gender'] = ds['Gender'].fillna(method  = 'ffill')'''


ds['Total_Mark(%)'] = (ds['History'] + ds['Science'] + ds['Maths']+ ds['English'])/4


ds['Result'] = ['Pass' if mark > 40 else 'Fail' for mark in ds["Total_Mark(%)"]]


ds['Performance'] = ['Bad' if mark < 36 else 'Good' if mark >36 and mark < 79 else 'Excellent' for mark in ds['Total_Mark(%)'] ]
print(ds)

dsa = (ds['Performance'] == 'Bad').sum()
print(dsa)

ds.to_csv('D:\PythonProgramming\prepML\day9\marksheet.csv',index = False)


print(ds.columns)