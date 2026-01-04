import pandas as pd

data = pd.DataFrame({
    'Name':["Ram",'Dinesh','Kumar','Khabar'],
    'Science_mark' : [29,98,68,88],
    'Maths_mark' : [79,14,57,89],
    'Overall_result': ['Pass','Fail','Pass','Pass'],
    'Performance' : ['Bad','Good','Good','Excellent']
})

print(data['Science_mark'].mean())
print(data.info())
print(data['Overall_result'].describe())
print(data['Performance'].describe())