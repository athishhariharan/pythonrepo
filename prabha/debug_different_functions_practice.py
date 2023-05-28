# Debugging a Loop

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    # Set a breakpoint on this line to pause the execution for each iteration
    result = num * 2
    print(result)


# Debugging an If-Else Condition

num1 = 10
num2 = 5

# Set a breakpoint on this line to pause the execution before the if-else condition
if num1 > num2:
    result = num1 - num2
else:
    result = num1 + num2

print(f"The result is: {result}")



# Debugging a While Loop

count = 0

while count < 5:
    # Set a breakpoint on this line to pause the execution within the loop
    print(f"Count: {count}")
    count += 1



# Debugging a List Comprehension

numbers = [1, 2, 3, 4, 5]

# Set a breakpoint on this line to pause the execution within the list comprehension
squared_numbers = [num ** 2 for num in numbers]

print(squared_numbers)



# Debugging a Dictionary

student_scores = {"Alice": 85, "Bob": 90, "Charlie": 78, "Dave": 92}

for name, score in student_scores.items():
    # Set a breakpoint on this line to pause the execution within the loop
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"

    print(f"{name}: {score} - Grade: {grade}")



# Debugging a Try-Except Block

num1 = 10
num2 = 0

try:
    # Set a breakpoint on this line to pause the execution within the try block
    result = num1 / num2
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero")



# Debugging a List Manipulation

numbers = [1, 2, 3, 4, 5]

# Set a breakpoint on this line to pause the execution before modifying the list
numbers.append(6)

# Set a breakpoint on this line to pause the execution before printing the modified list
print(numbers)


