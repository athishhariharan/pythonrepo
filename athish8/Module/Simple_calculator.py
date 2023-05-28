def calculate():
    num1 = int(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    num2 = int(input("Enter the second number: "))

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
        return None

    return result

# Example usage
calculation_result = calculate()
if calculation_result is not None:
    print("The result is:", calculation_result)
