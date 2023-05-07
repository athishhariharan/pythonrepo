# Define a list of numbers
# Initialize a variable to hold the sum of the positive numbers
# Loop through the list using a for loop
# Check if the current number is positive
# If the current number is positive, add it to the positive_sum variable
# After the loop, the positive_sum variable will hold the sum of the positive numbers
numbers = [-2,5,3,-8,10,7,-4]
positive_sum = 0
for num in numbers:
    if num > 0:
        positive_sum += num
print(f"The sum of the positive number in the list is {positive_sum}.")