import pandas as pd

data = pd.DataFrame({
    'Name':["Ram",'Dinesh','Kumar','Khabar'],
    'Science_mark' : [29,98,68,88],
    'Maths_mark' : [79,14,57,89],
    'Overall_result': ['Fail','Fail','Pass','Pass']
})

data['Total_percent'] = (data['Science_mark'] + data['Maths_mark'])/2


data['Result_Science'] = ['Pass' if Science_mark >35 else 'Fail' for Science_mark in data['Science_mark']]


data['Result_Maths'] = ['Pass' if mark >= 35 else 'Fail' for mark in data['Maths_mark']]

data["Performance"] = ['Low' if mark < 60 else 'Medium' if mark > 61 and mark < 80 else 'High'  for mark in data['Total_percent']]

