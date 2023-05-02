# Initialize variable 'sum' to 0
# Iterate over each element 'num' in list using for loop
# Add 'num' to 'sum'
# After using loop, divide 'sum' by length of list to get average
# Return and print average
def average(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum / len(numbers)
my_numbers = [1, 2, 3, 4, 5]
my_average = average(my_numbers)
print(my_average)
