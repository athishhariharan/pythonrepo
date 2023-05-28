# Simple Calculator Program for Beginners

# Addition
def add(num1, num2):
    return num1 + num2

# Subtraction
def subtract(num1, num2):
    return num1 - num2

# Multiplication
def multiply(num1, num2):
    return num1 * num2

# Division
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero!"

# Get the input
num1 = float(input("Enter the first number: "))
operation = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculator operation based on the operator
if operation == "+":
    result = add(num1, num2)
    print("The sum is:", result)
elif operation == "-":
    result = subtract(num1, num2)
    print("The difference is:", result)
elif operation == "*":
    result = multiply(num1, num2)
    print("The product is:", result)
elif operation == "/":
    result = divide(num1, num2)
    print("The quotient is:", result)
else:
    print("Invalid operator! Please enter a valid operator.")

