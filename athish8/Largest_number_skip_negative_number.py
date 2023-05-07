# Take input from the user
# Initialize the largest number to the first non-negative number in the list
# Find the largest number in the list while skipping negative numbers
# Skip negative numbers
# Check if the current number is larger than the current largest number
# Print the largest number
num_list = [3,-2,10,15,-8,9]
largest_num = float('-inf')
for num in num_list:
    if num >= 0 and num > largest_num:
        largest_num = num 
print(f"The largest number in the list is:{largest_num}")