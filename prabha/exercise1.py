# this program for simple calculator
# author: prabha subbaian
# 


# get the two float inputs from user
# get the operator input from user for operation
# operation: add, sub, multiplication, division
# Validate the input using if condition then proceed respective operation
# if user input is + i have to execute add operation
# if user input is - I have to exeucte sub operation
# if muser input is * I have to execute mul operation
# if user input is / I have to execute div operation
# Enter the correct operator and exit



# get the input

num1 = float(input("Enter a first number: "))
operation = input("Enter the operator(+,-,*,/): ")
num2 = float(input("Enter a second number: "))


# Calculator operation
if operation == "+":
    # add two numbers
    result = num1 + num2
    print("The sum is: ", result)
elif operation == "-":
    # subtract two numbers
    result = num1 - num2
    print("The subtract is: ", result)
elif operation == "*":
    # multiply two numbers
    result = num1*num2
    print("The multiply is: ", result)
elif operation == "/":
    # divide two numbers
    result = num1/num2
    print("The divide is: ", result)
else:
    print("Enter the correct operation")
    exit()











