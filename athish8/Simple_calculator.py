num1 = int(input("Enter the first number:"))
operation = input("Enter the operation(+,-,*,/):")
num2 = int(input("Enter the second number:"))
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Invalid operation.")
print("Result:", result)