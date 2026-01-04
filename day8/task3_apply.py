import pandas as pd

data = pd.DataFrame({
    'Employee' : ['Ram','Steve','Dustin','Sink'],
    'Dept' : ['IT','HR','IT','Digital Marketing'],
    'Salary' : [55000,53000,65000,57000]

})

lb = lambda x : x + 5000

data['Updated_Salary'] = data['Salary'].apply(lb)



print(data)