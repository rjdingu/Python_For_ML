import pandas as pd
data = pd.read_csv('D:\PythonProgramming\prepML\day4\data.csv')
'''
In python : Logical operator = and,or
In pandas  : Logical Operator = || &'''

# Filtering ....
print("Filtering process : ")
fil = data[(data['Pulse']>120) & (data['Maxpulse'] > 100)]
print(fil)

# Selection...
sel = data[['Date','Duration']]

print("Selection Process :")
print('\n',sel)