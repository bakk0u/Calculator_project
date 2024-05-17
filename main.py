from art import logo
import math
import os
import matplotlib.pyplot as plt
import numpy as np

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

def exponential(n1):
    return math.exp(n1)

def logarithm(n1, n2=None):
    if n1 <= 0:
        return "Error: Logarithm undefined for non-positive numbers"
    if n2:
        return math.log(n1 + n2)
    return math.log(n1)

def cosine(n):
    return math.cos(math.radians(n))

def sine(n):
    return math.sin(math.radians(n))

def tangent(n):
    return math.tan(math.radians(n))

def logadd(n1, n2):
    if n1 <= 0 or n2 <= 0:
        return "Error: Logarithm undefined for non-positive numbers"
    return math.log(n1 + n2)

def addlog(n1, n2):
    if n1 <= 0 or n2 <= 0:
        return "Error: Logarithm undefined for non-positive numbers"
    return n1 + n2

def addcos(n1, n2):
    return math.cos(math.radians(n1)) + math.cos(math.radians(n2))

def addsin(n1, n2):
    return math.sin(math.radians(n1)) + math.sin(math.radians(n2))

def addtan(n1, n2):
    return math.tan(math.radians(n1)) + math.tan(math.radians(n2))

def addexp(n1, n2):
    return math.exp(n1) + math.exp(n2)

def choose_operation(operand1, operation, operand2=None):
    global calculation_number
    if operation == "+":
        return add(operand1, operand2)
    elif operation == "-":
        return subtract(operand1, operand2)
    elif operation == "*":
        return multiply(operand1, operand2)
    elif operation == "/":
        return divide(operand1, operand2)
    elif operation == "^":
        return exponential(operand1)
    elif operation == "log":
        return logarithm(operand1, operand2)
    elif operation == "cos":
        return cosine(operand1)
    elif operation == "sin":
        return sine(operand1)
    elif operation == "tan":
        return tangent(operand1)
    elif operation == "logadd":
        return logadd(operand1, operand2)
    elif operation == "addlog":
        return addlog(operand1, operand2)
    elif operation == "addcos":
        return addcos(operand1, operand2)
    elif operation == "addsin":
        return addsin(operand1, operand2)
    elif operation == "addtan":
        return addtan(operand1, operand2)
    elif operation == "addexp":
        return addexp(operand1, operand2)
    elif operation == "plot":
        plot_function()
        return None

def plot_function():
    expression = input("Enter a mathematical expression (e.g., 'x**2 + 2*x + 1'): ")
    try:
        x = np.linspace(-10, 10, 400)
        y = eval(expression)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Plot of {expression}')
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error: {e}")

# Initialize the dictionary and variable for calculation logs
calculations_log = {}
calculation_number = 1

print(logo)

while True:
    operation = input("Pick an operation (+, -, *, /, ^ (exponential), log (logarithm), cos (cosine), sin (sine), tan (tangent), logadd (logarithm of the sum), addlog (sum of logarithms), addcos (sum of cosines), addsin (sum of sines), addtan (sum of tangents), addexp (sum of exponentials), plot (plot a function)): ")

    if operation == "plot":
        choose_operation(None, operation)
        continue

    first_number = float(input("What is the first number?: ")) if operation not in ["plot"] else None

    if operation in ["^", "log"]:
        result = choose_operation(first_number, operation)
    elif operation in ["cos", "sin", "tan", "logadd", "addlog", "addcos", "addsin", "addtan", "addexp"]:
        second_number = float(input("What is the second number?: "))
        result = choose_operation(first_number, operation, second_number)
    else:
        second_number = float(input("What is the second number?: "))
        result = choose_operation(first_number, operation, second_number)

    if isinstance(result, str):  # Check if the result is an error message
        print(result)
    elif result is not None:
        print(f"{first_number} {operation} {second_number if operation not in ['^', 'log', 'cos', 'sin', 'tan', 'logadd', 'addlog', 'addcos', 'addsin', 'addtan', 'addexp', 'plot'] else ''} = {result}")

    to_continue = input(f"Type 'y' to continue calculating, 'n' to start a new calculation, or 'q' to quit: ").lower()
    if to_continue == 'n':
        clear()
    elif to_continue == 'q':
        print("Goodbye!")
        break
