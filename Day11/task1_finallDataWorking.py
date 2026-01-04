import pandas as pd
import numpy as np

d = pd.read_csv('D:\PythonProgramming\prepML\Day11\Heart_Disease_Prediction.csv')


d = d.drop('Chest pain type',axis = 1)


d = d.sort_values('Heart Disease',ascending = False)

d['Sex'] = d['Sex'].astype(str)


d['Sex'] = ['Male' if i == '1' else 'Female' for i in d['Sex']]


#d_grpby = d.groupby(['Sex','Heart Disease','BP Level']).size()
#print(d_grpby)

d['BP Level'] = ['High BP' if x > 150 else 'Moderate' if x < 151 and x > 120 else 'No Risk'  for x in d['BP']]


d['Cholestrol Level'] = ['Risk' if x > 249 else 'Cautious' if x > 200 and x < 250 else 'Normal' for x in d['Cholesterol'] ]
#print(d)

d_grpby = d.groupby(['Sex','Heart Disease','BP Level','Cholestrol Level']).size()
print(d_grpby)


d.to_csv('D:\PythonProgramming\prepML\Day11\Heart_Disease_Prediction.csv')