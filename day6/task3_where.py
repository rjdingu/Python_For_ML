import numpy as np

# Print pass if mark > 50 or else fail

marks = [54,75,13,46,48,35,70,40,78,80,89,56,79]
marks = np.array(marks)
result = np.where(marks >= 45 , 'Pass',"Fail")
print(result)

# If mark less than 40 mention as 40 
grace_marks = np.where(marks < 40 , 40 , marks)
print(grace_marks)

# Difference between loop and Where in numpy
Newresult = []
for i in marks :
    if i  < 40 : 
        Newresult.append(40)
    else:
        Newresult.append(i)

print(Newresult)