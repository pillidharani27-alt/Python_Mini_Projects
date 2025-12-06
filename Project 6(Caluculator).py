import os
def add(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
operation_dict={"+":add,
                "-":substraction,
                "*":multiply,
                "/":division
                }
def calculator():
    num1=float(input("Enter first number: "))
    for symbol in operation_dict:
         print(symbol)
    continue_flag=True
    while continue_flag:
       op_symbol=input("pick an operation\n")
       num2=float(input("Enter second number: "))
       calculator_fun=operation_dict[op_symbol]
       output=calculator_fun(num1,num2)
       print(f"{num1}{op_symbol}{num2}={output}")
       should_continue=input("Enter 'y' to continue caluculation with{output} or 'n' to start new caluculation or 'x' to exit\n").lower()
       if should_continue=='y':
          num1=output
       elif should_continue=='n':
           continue_flag=False
           os.system('cls')
           calculator()
       else:
           continue_flag=False
           print("bye")
calculator()
