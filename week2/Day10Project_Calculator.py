
from Day10_logo import logo

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

def calculator():
    should_continue = False
    while not should_continue:
        print(logo)
        num1 = int(input("What's the first number?"))
        print("+\n-\n*\n/")
        operation = input("Pick an operation from the line above")
        num2 = int(input("What's the next number?"))
        operations = {"+":"add","-":"subtract","*":"multiply", "/":"divide"}
        function = operations[operation]
        val = eval(function + "(num1,num2)")
        print(f"{num1} {operation} {num2} = {val}")
        another = input("Do you wish to do another operation, type 'yes' or 'no'?")
        if another == "no":
            should_continue = True