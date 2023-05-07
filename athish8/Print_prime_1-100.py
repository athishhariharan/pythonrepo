# Loop through the numbers from 1 to 100 using a for loop 
# Assume that the current number is prime
# Check if the current number is divisible by any number other than 1 and itself
# If the current number is divisible by any other number, it is not prime
# If the current number is prime, print it
for num in range(1,101):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print(num)
