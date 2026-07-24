a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
def cal(a, b):
    add= a + b
    sub= a - b
    mul= a * b
    div= a / b
    return add, sub, mul, div
c=input("Enter your choice: add, sub, mul, div: ")
if c=="add":
    print("Addition: " + str(cal(a, b)[0]))         
elif c=="sub":
    print("Subtraction: " + str(cal(a, b)[1]))
elif c=="mul":  
    print("Multiplication: " + str(cal(a, b)[2]))
elif c=="div":
    print("Division: " + str(cal(a, b)[3]))
    
