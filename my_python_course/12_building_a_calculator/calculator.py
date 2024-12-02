# Building a calculator 


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == '+':
    print("Result:", add(num1, num2))
elif operator == '-':
    print("Result:", subtract(num1, num2))
elif operator == '*':
    print("Result:", multiply(num1, num2))
elif operator == '/':
    print("Result:", divide(num1, num2))
else:
    print("Invalid operator")
