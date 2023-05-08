# Define a list of numbers
# Initialize the variables to hold the smallest and second smallest numbers
# Loop through each number in the list
# Check if the current number is smaller than the smallest number so far
# Check if the current number is greater than the smallest number but smaller than the second smallest number
# Print the second smallest number
num_list = [5,2,8,3,1,9]
smallest = num_list[0]
second_smallest = num_list[0]
for num in num_list:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
print("The second smallest number is:", second_smallest)