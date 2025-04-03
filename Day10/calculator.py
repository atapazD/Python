def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    shouldAccumulate = True
    firstNum=float(input("What is the first number:\n"))

    while shouldAccumulate:

        mathOp= input("Please select +, -, / , * : \n")
        secondNum = float(input("What is the second number:\n"))
        operator= {"+": add, "*": multiply, "/": divide, "-": subtract}

        result = operator[mathOp](firstNum,secondNum)
        print(f"{firstNum}{mathOp}{secondNum}={result}")

        choice = input (f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation")

        if choice == 'y':
            firstNum = result
        else:
            shouldAccumulate = False
            print("\n" * 20)

calculator()