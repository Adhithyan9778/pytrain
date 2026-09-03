a=int(input("Enter the first number"))
operator=input("Enter the operator")
b=int(input("Enter the second number"))


def calculate(a,operator,b):

    if operator=="+":
        print(a+b)
    elif operator=="-":
        print(a-b)
    elif operator=="*":
        print(a*b)
    elif operator=="/":
        try:
            print(a/b)
        except ZeroDivisionError:
            print("invalid")
    else:
        print("not valid operator")
calculate(a,operator,b)
        
    
