# Take two numbers as input
# Define a list of operations to perform
# Loop through the operations
# Perform the operation and print the result
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operations = ["+","-","*","/"]
for op in operations:
    if op == "+":
        print(num1,"+",num2,"=",num1+num2)
    elif op == "-":
        print(num1,"-",num2,"=",num1-num2)
    elif op == "*":
        print(num1,"*",num2,"=",num1*num2)
    elif op == "/":
        print(num1,"/",num2,"=",num1/num2)


