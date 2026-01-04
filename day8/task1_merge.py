import pandas as pd
# Employess Name
employees = pd.DataFrame({
    'EmpID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'DeptID': [1, 2, 2, 4]  
})

# DataFrame 2: Department Names
departments = pd.DataFrame({
    'DeptID': [1, 2, 3],
    'DeptName': ['HR', 'IT', 'Marketing']  
})

merged = pd.merge(employees,departments,on = 'DeptID')
print(merged)

print("\nINNER :\n")
inner_merge = pd.merge(employees,departments,how = 'inner',on = 'DeptID')
print(inner_merge)

print("\nOUTER :\n")
outer_merge = pd.merge(employees,departments,how= 'outer', on = 'DeptID')
print(outer_merge)


# Concating two table...

print('\n Concat ROWS: \n')
conat_rows = pd.concat([employees,departments],axis= 0)
print(conat_rows)

print('\n CONCST COLUMNS : \n')
concat_col = pd.concat([employees,departments], axis = 1)
print(concat_col)