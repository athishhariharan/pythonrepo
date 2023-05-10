# Define a list of numbers
# Loop through each number in the list
# Check if the current number is divsible by both 2 and 3
# If it is, print the number
num_list = [10,12,15,18,20,24,30,35]
for num in num_list:
    if num % 2 == 0 and num % 3 == 0:
        print(num)