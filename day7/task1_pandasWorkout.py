import pandas as pd

data = pd.read_csv('D:\PythonProgramming\prepML\day7\marksheet.csv')
#print(data)


# Printing the head 
hd = data.head()
print(hd)
# Printing the last data from the csv file
tl = data.tail(7)
print(tl)
# To find the shape of the csv file
shap = data.shape
print(shap)
# To get the columns of the csv files
col = data.columns
print(col)
# Info
inf =data.info()
print(inf)