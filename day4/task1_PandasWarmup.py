import pandas as pd 
# Create a sample dataFrame...
data = {
    'Name' : ['Raj','Harsih','Kavin','Pavan'],
    'Age' :  [18,19,19,18],
    'TotalMark' : [76,87,89,79]
}

d = pd.DataFrame(data,index = [i for i in range(1,5)])

print(d.head(2))
print(d.columns)
print(d.shape)

# Import a csv data ... 
csv = pd.read_csv('D:\PythonProgramming\prepML\day4\data.csv')


print(csv.head(10))
print(csv.info())
print(csv.describe())