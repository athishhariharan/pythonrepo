# Ask user to enter 'n's value
# Initialize variable 'min_num' to -infinity
# Use for loop to take 'n' input from user and compare with 'min_num'
# If input number is greater 'min_num', update 'min_num'
# Print the minimum number
n = int(input("Enter the value of n: "))
min_num = float('inf')

for i in range(n):
    num = float(input("Enter a number: "))
    if num < min_num:
        min_num = num

print("The minimum number is", min_num)