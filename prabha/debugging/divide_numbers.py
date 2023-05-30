# Define a function to perform division
def divide_numbers(a, b):
    try:
        # Perform division
        result = a / b
        return result
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Division by zero is not allowed.")

# Set numerator and denominator values
numerator = 10
denominator = 0

# Call the divide_numbers function and store the result
result = divide_numbers(numerator, denominator)

# Check if the result is not None and print it
if result is not None:
    print("The result is:", result)
