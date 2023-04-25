# Initialize a variable 'n number to calculate factorial of 5
# Initialize a variable 'factorial' to 1
# Loop from 1 to n- variable
# Multiply 'factorial' by each number from 1 to n
# Print result

# Static
# n = 5
# factorial = 1
# for num in range(1,6):
#     factorial *= num
# print(factorial)

# Dynamic
n = int(input("Enter a number:"))
factorial = 1
for num in range(1,n + 1):
    factorial *= num
print(factorial)
