# Ask user to enter 'n's value
# Initialize variable 'max_num' to -infinity
# Use for loop to take 'n' input from user and compare with 'max_num'
# If input number is greater 'max_num', update 'max_num'
# Print the maximum number
n = int(input("Enter the value of n: "))
max_num = -float('inf')

for i in range(n):
    num = float(input("Enter a number: "))
    if num > max_num:
        max_num = num

print("The maximum number is", max_num)