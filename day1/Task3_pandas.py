# Import pandas and get a csv file
import pandas as pd
print(pd.__version__)
filePath = 'D:\PythonProgramming\Challenges\day1\data.csv'
data = pd.read_csv(filePath,index_col='Duration')



# Show First Five Rows
print(data[0:5])

# Show Column names
print(data.columns)

# Correct the Missing values
data = data.dropna(subset = ["Calories"])

data['Date'] = data['Date'].ffill()

# Describe the data
print(data.describe())


#Filter the data
high_calories = data[data['Calories']> 400]
print(high_calories)