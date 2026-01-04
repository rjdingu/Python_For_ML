# Division by 0

try : 
    a = int(input("Enter a number : "))
    b = int(input("Enter a nuber : "))
    print(a/b)

except ZeroDivisionError as z:
    print("Don't use 0 in the second variable....",'\n',z) 



# File not Found ..
try :
    f = open("Names.txt",'r')
    print(f.read())
    f.close()

except FileNotFoundError:
    print("The Entered File Doesn't Exist ...")


# Create own Exception

class AgeNotEligible(Exception):
    'Your Age is below 18'
    pass

try : 
    age = int(input("Enter your age : "))
    if age < 18 :
        raise AgeNotEligible
    
except AgeNotEligible as a :
    print("Age is ineligible")

else :
    print("Your eligible for voting .... \n Thank you !")