def calci(a,b,operator):
    if operator == '+':
        print(a+b)
    if operator == '-':
        print(a-b)
    if operator == '*':
        print(a*b)
    if operator == '/':
        try:
            print(a/b)
        except ZeroDivisionError :
            print("Zero is use in denominator....")

    if operator == '^':
        print(a**b)


