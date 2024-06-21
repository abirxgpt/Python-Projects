#CAlCULATOR
import math

#add
def add(n1,n2):
    n = n1 + n2
    return n

#subtract
def subtract(n1,n2):
    n = n1 - n2
    return n

#multiply
def multiply(n1,n2):
    n = n1 * n2
    return n

#divide
def divide(n1,n2):
    n = n1/n2
    return n

#exponential
def expo(n1,n2):
    n = n1 ** n2
    return n

#Square root
def sqrt(n1,n2):
    n = n1 ** 0.5
    return n


#Dictionary
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "^" : expo,
    "square root" : sqrt
}

run = "n"

def new():
    num1 = float(input("What is the First Number?: "))
    for i in operations:
        print(i)
    opr = input("Choose any Operation: ")
    num2 = float(input("What is the Second Number?: "))
    todo = operations[opr]
    answer = todo(n1=num1, n2=num2)
    print(f"{num1} {opr} {num2} = {answer}")
    return answer

def old():
    print(f"The First Number is: {ans}")
    for i in operations:
        print(i)
    opr = input("Choose any Operation: ")
    num2 = float(input("What is the Second Number?: "))
    todo = operations[opr]
    new_answer = todo(n1=ans, n2=num2)
    print(f"{ans} {opr} {num2} = {new_answer}")
    return new_answer

while run == 'y' or run == 'n': 
    if run == "y":
        ans = old()
    elif run == "n":
        ans = new()
        
    run = input(f'\nEnter "y" if you want to keep Calculation with {ans} \nor "n" if you want to do a new calculation \nor else Enter "x" to stop the operation: ').lower()
