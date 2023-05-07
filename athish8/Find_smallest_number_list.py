# Define a list of numbers
# Assume that the first number in the list is the smallest
# Loop through the list using a for loop and compare each number to the current smallest number
# If the current number is smaller than the current smallest number, update the smallest number to be the current number
# After the loop, the smallest_number variable will hold the smallest number in the list
numbers = [5,8,3,2,7,1]
smallest_number = numbers[0]
for num in numbers:
    if num < smallest_number:
        smallest_number = num
print(f"The smallest number in the list is {smallest_number}")