# Create a list , tuple , set ,dict

l1 = list(map(int,input("Enter the list  :").split()))
print(l1)

t1 = tuple(map(int,input("Enter the values  :").split()))
print(t1)

s1 = set(map(int,input("Enter the set values :").split()))
print(s1)


d = {}
key = 0
for i in range(5):
    value = int(input("Enter the values for dict : "))
    d[key] = value
    key = key+ 1
print(d)
  
# Create a function that takes list and print event number of the list
def even_num():
    l = [1,5,32,56,23,78]
    l1 = []
    for x in l:
        if x%2 == 0 :
            l1.append(x)
    print(l1)
    return l1

even_num()


# Square using Lambda 
def square_lambda():

        l = [34,2,3,4,5]
        l2 = []
        square = lambda x : x*x
        for i in l:
            x = (square(i))
            l2.append(x)

        print(l2)

square_lambda()


# List thst divisible by 3
def divisibleBy3():
    l1 = []
    for i in range(1,20):
        if i % 3 == 0:
            l1.append(i)

    print(l1)

divisibleBy3()
