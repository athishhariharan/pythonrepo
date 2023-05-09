# Define a list of numbers
# Loop through each number in the list
# Check if the number is greater than 1
# Loop through all the numbers from 2 to the number itself
# Check if the number is divisible by any other number except 1 and itself
# If the number is not divisible by any other number except 1 and itself, it is prime,so print
num_list = [3, 4, 5, 6, 7, 8, 9]

for num in num_list:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
