# Simple command-line calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

def power(a, b):
    return a ** b

OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide, "^": power}

if __name__ == "__main__":
    a = float(input("First number: "))
    op = input("Operation (+ - * / ^): ")
    b = float(input("Second number: "))
    print("Result:", OPERATIONS[op](a, b))
