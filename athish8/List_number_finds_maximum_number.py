# Define a list of numbers
# Initialize a variable to hold the maximum number
# Loop through the list using a for loop
# Check if the current number is greater than the maximum number
# If the current number is greater than the maximum number, set it as the new maximum number
# After the loop, the max_num variable will hold the maximum number in the list.
numbers = [3,9,1,7,5,2,8]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"The maximum number in the list is {max_num}.")
