import pandas as pd

data = pd.read_csv('D:\PythonProgramming\prepML\day12\heart_disease_health_indicators_BRFSS2015.csv')


data = data.apply(lambda col : col.astype(str) if col.dtype == 'float' else col )


data['HeartDiseaseorAttack'] = ['Yes' if x == '1.0' else 'NO' for x in data['HeartDiseaseorAttack']]
data['HighBP'] = ['Yes' if x == '1.0' else 'NO' for x in data['HighBP']]
data['HighChol'] = ['Yes' if x == '1.0' else 'NO' for x in data['HighChol']]
data['Risk'] =  ['High Risk' if x == 'Yes' else 'Nothing yet' for x in data['HeartDiseaseorAttack']]

print(data)

print(data['Risk'].value_counts())