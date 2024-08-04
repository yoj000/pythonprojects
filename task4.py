def calculator():
    a=float(input("enter a first number"))
    b=float(input("enter a second number"))
    operator=input("enter an operator(+,-,*,%,/):")
    if operator=="+":
        result=a+b
    elif operator=="-":
        result=a-b 
     elif operator=="*":
        result=a*b 
     elif operator=="%":
        result=a%b 
     elif operator=="/":
        if b!=0:
           result=a/b  
        else:
            return "error"
    else:
        return "invalid operator"
    return f"The result of{a} {operator} {b} is :{result}"
print(calculator)                

