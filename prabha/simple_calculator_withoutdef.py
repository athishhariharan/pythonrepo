# Simple Calculator Program for Beginners

# Get the input
num1 = float(input("Enter the first number: "))
operation = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculator operation
if operation == "+":
    result = num1 + num2
    print("The sum is:", result)
elif operation == "-":
    result = num1 - num2
    print("The difference is:", result)
elif operation == "*":
    result = num1 * num2
    print("The product is:", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("The quotient is:", result)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator! Please enter a valid operator.")


