# Import the starting logo 
from art import logo
# clear the console for new calculations
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# creating the first basic functions for the different arithemetic operations 
def add(n1,n2):
    result = float(n1) + float(n2)
    return float(result)
def substract(n1, n2):
    result = float(n1) - float(n2)
    return float(result)
def multiply(n1, n2):
    result = float(n1) * float(n2)
    return float(result)
def divide(n1, n2):
    result = float(n1) / float(n2)
    return float(result)
# creating a dictionary to record the operations
calculations_log = {}
calculation_number = 1
#Create a function which take care of which operation is chosen
def choose_operation(operand1, opeartion, operand2):
    global calculation_number # This tells the function to look for the variable globaly not only locally 
    if operation == "+":
        result = add(operand1, operand2)
        calculations_log[calculation_number] = result
        calculation_number += 1
    elif operation == "-":
        result = substract(operand1, operand2)
        calculations_log[calculation_number] = result
        calculation_number += 1
    elif operation == "*":
        result = multiply(operand1, operand2)
        calculations_log[calculation_number] = result
        calculation_number += 1
    elif operation == "/":
        result = divide(operand1, operand2)
        calculations_log[calculation_number] = result
        calculation_number += 1
    return result 
# ask the user for the operands and the disired operation
print(logo)
first_number = float(input("What is the first number?: "))
print("+\n-\n*\n/")
operation = input("Pick an operation: ")
second_number = float(input("What is the second number?: "))
to_continue = "y"
result = float(choose_operation(first_number, operation, second_number))
print(f"{first_number} {operation} {second_number} = {result}") 
to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 'q' to quit: ").lower()
while True:
    if to_continue == 'y':
        operation = input("Pick an operation: ")
        next_number = float(input("What is the next number: "))
        result = choose_operation(calculations_log[calculation_number - 1], operation, next_number)
        print(f"{calculations_log[calculation_number - 2]} {operation} {next_number} = {result}")
        to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 'q' to quit: ").lower()
    elif to_continue == 'n':
        clear()
        print(logo)
        calculations_log = {}
        to_continue = 'y'
        calculation_number = 1
        first_number = float(input("What is the first number?: "))
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        second_number = float(input("What is the second number?: "))
        to_continue = "y"
        result = float(choose_operation(first_number, operation, second_number))
        print(f"{first_number} {operation} {second_number} = {result}") 
        to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 'q' to quit: ").lower()
    elif to_continue == 'q':
        print("Goodbye!")
        break
