# step over
# def multiply(a, b):
#     result = a * b
#     return result

# num1 = 5
# num2 = 2

# result = multiply(num1, num2)  # Set a breakpoint on this line
# print(result)

# # or
# num1 = 5
# num2 = 2

# result = num1 * num2  # Set a breakpoint on this line
# print("The result is:", result)

# step into
# def multiply(a, b):  # Set a breakpoint on this line
#     result = a * b
#     return result

# num1 = 5
# num2 = 2

# result = multiply(num1, num2)
# print(result)

# or
# num1 = 5
# num2 = 2

# result = num1 * num2  # Set a breakpoint on this line
# print("The result is:", result)


# step out
# def multiply(a, b):
#     result = a * b  # Set a breakpoint on this line
#     return result

# def calculate():
#     num1 = 5
#     num2 = 2

#     result = multiply(num1, num2)
#     print(result)

# calculate()

# continue
# def multiply(a, b):
#     result = a * b
#     return result

# num1 = 5
# num2 = 2

# result = multiply(num1, num2)  # Set a breakpoint on this line
# print(result)



# step over
def factorial(n):
    if n == 0:
        return 1
    else:
        # set breakpoint
        return n * factorial(n - 1) 

result = factorial(5)
print(result)

# step over
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)# Set a breakpoint on this line

print(squared_numbers)

# step in
def calculate_average(numbers):
    total = sum(numbers)# Set a breakpoint on this line
    average = total / len(numbers)
    return average

grades = [85, 90, 92, 88, 95]
average_grade = calculate_average(grades)
print("Average Grade:", average_grade)

#  step over
def is_prime(number):
    if number < 2:
        return False# Set a breakpoint on this line
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

number = 17
is_prime_number = is_prime(number)
print(f"{number} is prime:", is_prime_number)

# step over
def find_max(numbers):
    if not numbers:
        return None
    max_value = numbers[0]# Set a breakpoint on this line
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

numbers = [10, 5, 8, 12, 3]
max_number = find_max(numbers)
print("Max number:", max_number)

# step over
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num # Set a breakpoint on this line
    return total

numbers = [1, 2, 3, 4, 5]
sum_result = calculate_sum(numbers)
print("Sum:", sum_result)


