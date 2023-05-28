# Script-Level Debugging Example
# step over
# Define a function to check if a number is even
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Generate a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterate through the list and print whether each number is even or odd
for num in numbers:
    # Set a breakpoint on the line below to pause the execution
    if is_even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


# Function-Level Debugging Example
#  debugging controls to step into
# Define a function to calculate the average of a list of numbers
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Create a list of numbers
numbers = [10, 20, 30, 40, 50]

# Call the calculate_average function and assign the result to a variable
# Set a breakpoint on the line below to pause the execution
result = calculate_average(numbers)

# Print the result
print(f"The average is: {result}")


# Module-Level Debugging Example
#  debugging controls to step over 
# Define a module-level variable
message = "Hello, World!"

# Define a function to print the message
def print_message():
    # Set a breakpoint on the line below to pause the execution
    print(message)

# Call the print_message function
print_message()



# Class-Level Debugging Example
# debugging controls to step over
class Rectangle:
    def __init__(self, width, height):
        # Set a breakpoint on the line below to pause the execution
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area

# Create an instance of the Rectangle class
rectangle = Rectangle(5, 3)

# Call the calculate_area method
# Set a breakpoint on the line below to pause the execution
result = rectangle.calculate_area()

# Print the result
print(f"The area of the rectangle is: {result}")


# Complex Program Debugging Exercise
# debugging controls to step over
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        # Set a breakpoint on the line below to pause the execution
        factorial *= i
    return factorial

def calculate_sum_of_factorials(numbers):
    sum_of_factorials = 0
    for num in numbers:
        # Set a breakpoint on the line below to pause the execution
        factorial = calculate_factorial(num)
        sum_of_factorials += factorial
    return sum_of_factorials

# Set a breakpoint on the line below to pause the execution
numbers = [3, 4, 5, 6, 7]

result = calculate_sum_of_factorials(numbers)

print(f"The result is: {result}")


