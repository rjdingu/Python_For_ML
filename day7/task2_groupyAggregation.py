import pandas as pd

data = pd.read_csv('D:\PythonProgramming\prepML\day7\marksheet.csv')



group_section = data.groupby('Section').agg({'Science' : ['mean','count','max','min'],'English' :  ['mean','count','max','min'],'History' :  ['mean','count','max','min'],'Maths' :  ['mean','count','max','min']})

print(group_section)

group_gender = data.groupby('Gender').agg({'Science': ['mean','count','max','min'],'English': ['mean','count','max','min'],'History': ['mean','count','max','min'],'Maths': ['mean','count','max','min']}) 
print(group_gender)


group_gender_section = data.groupby(['Gender','Section']).agg({'Science': ['mean','count','max','min'],'English': ['mean','count','max','min'],'History': ['mean','count','max','min'],'Maths': ['mean','count','max','min']}) 
print(group_gender_section)
