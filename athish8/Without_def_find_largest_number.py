# Define a list of numbers named 'numbers'
# Initialize a variable named largest with the first element in the list of numbers
# Iterate over each element in the list of numbers using a for loop and a loop variable to the current number
# Check if the current number is larger than the largest variable
# If the current number is larger than the largest variable, update the largest variable to the current number
# Add iterating over all the elements in the list, largest variable will contain the largest number
# Print the value of largest variable, which is the largest number in the list

numbers = [7,3,8,2,6,9]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
    print(largest)