# Define a list of numbers
# Initialize variables to hold the maximum and minimum numbers
# Loop through each number in the list
# Check if the current number is greater than the current maximum
# If it is, update the maximum
# Check if the current number is less than the current minimum
# If it is, update the minimum
# Calculate the difference between the maximum and minimum numbers
# Print the difference
num_list = [12, 5, 23, 8, 17, 9]
max_num = num_list[0]
min_num = num_list[0]

for num in num_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

diff = max_num - min_num
print(diff)
