# Take input from the user as a list of numbers
# Initialize the variable to store the sum
# Loop through each number in the list
# Convert the number from string to interger
# Add the number to the total
# Print the sum
num_list = input("Enter a list of numbers separated by space:").split()
total = 0
for num in num_list:
    num = int(num)
    total += num
print("The sum of the numbers in the list is:", total)
