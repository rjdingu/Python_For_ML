import pandas as pd

data = pd.read_csv('D:\PythonProgramming\prepML\day10\marksheet.csv')


target_y = data['Total_Mark(%)']
remaining_x = data[['Science','English','Maths','History']]

print('\n Shape of Targeted Column y : \n')
print(target_y.shape)

print('\n Shape of Remaining Column x : \n')
print(remaining_x.shape)

