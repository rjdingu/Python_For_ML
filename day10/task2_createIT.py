import numpy as np
import pandas as pd

data1 = pd.read_csv('D:\PythonProgramming\prepML\day10\marksheet.csv')



data1['Rank'] = data1['Total_Mark(%)'].rank(ascending = False , method = 'dense')

data1 = data1.sort_values(by = 'Total_Mark(%)',ascending = False)

data1.to_csv('D:\PythonProgramming\prepML\day10\marksheet.csv')
