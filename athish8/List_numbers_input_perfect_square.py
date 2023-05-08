# Define a list of numbers
# Loop through each number in the list
# Check if the square root of the current number is an integer
# If the square root is an integer, print the number
num_list = [1,4,8,16,22,36]
for num in num_list:
    if int(num ** 0.5) ** 2 == num:
        print(num)