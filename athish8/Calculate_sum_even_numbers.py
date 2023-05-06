# Define a list of numbers
# Initialize the sum to 0
# Loop over each number in the list
# Check if the number is odd
# If it's odd, skip to the next iteration
# If it's even, add it to the sum
# Print the final sum
numbers = [2,3,5,7,10,11,12,15]
sum = 0
for num in numbers:
    if num % 2 == 1:
        continue
    sum += num
    print(f"The sum of all even numbers is {sum}")