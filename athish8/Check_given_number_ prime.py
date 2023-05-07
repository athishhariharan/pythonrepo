# Take input from the user
# Initialize the flag variable
# Check if the number is greater than 1
# Loop through the numbers from 2 to num-1
# Check if 'num' is divisible by 1
# If yes, num is not prime
# Break out of loop
# If num is less than or equal to 1, it is not prime
# Print result
num = int(input("Enter a number: "))
is_prime = True
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
else:
    print(num, "is not a prime number.")
