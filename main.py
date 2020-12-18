from replit import clear
from art import logo

def add(a,b):
    """takes 2 arguments and returns the sum""" 
    return a+b
def subtract(a,b):
    """"takes 2 arguments and returns the difference"""
    return a-b
def multiply(a,b):
    """takes 2 arguments and returns the product"""
    return a*b
def divide(a,b):
    """takes 2 arguments and returns the quotient"""
    return a/b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def start_calc():
    print(logo)
    first_num = float(input("What's the first number?: "))
    for i in operations:
        print(i)
    should_continue = True
    while should_continue:
        operation = input("Pick an operation: ")
        another_num = float(input("Pick another number: "))
        answer = operations[operation](first_num,another_num)
        print(f"{first_num} {operation} {another_num} = {answer}")
        keep_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if keep_calculating == 'y':
            first_num = answer
        elif keep_calculating == 'n':
            clear()
            start_calc()

start_calc()
