# Define a list of numbers
# Loop through the list using a for loop
# Check if the current number is divisible by 3 or 5
# If the current number is divisible by 3 or 5, print it
numbers = [2,7,15,21,30,33,45]
for num in numbers:
    if num % 3 == 0 or num % 5 == 0:
        print(num)