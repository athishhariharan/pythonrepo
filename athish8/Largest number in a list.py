# Define a function 'find_largest' that takes a list of numbers as input.
# Initialize a variable 'largest' to be the first element of the list
# Loop over the remaining elements of the list using a 'for' loop.For each element: a. If the element is greater than the current value of 'largest', update the value of 'largest' to be the current element
# After the loop completes, return the value of 'largest' which is the largest number in the input list.
def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

numbers = [5,8,2,4,6,7]
largest_number = find_largest(numbers)
print(f"The largest number in {numbers} is {largest_number}")