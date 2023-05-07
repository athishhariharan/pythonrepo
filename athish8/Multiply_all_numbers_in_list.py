# Define the list of numbers
# Initiallize the product variable to 1
# Iterate over each number in the list
# Multiply the current number by the current product
# Print the final product
numbers = [2,4,6,8,10]
product = 1
for num in numbers:
    product *= num
print("The product of all the numbers is:", product)