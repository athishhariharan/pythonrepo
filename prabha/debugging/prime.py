# def check_prime(n):
#     if n < 2:  # Check if the number is less than 2
#         return False
#     for i in range(2, n):  # Iterate from 2 to n-1
#         if n % i == 0:  # Check if n is divisible by i
#             return False  # If divisible, n is not prime
#     return True  # If no divisor found, n is prime

# number = 12
# is_prime = check_prime(number)
# if is_prime:
#     print(number, "is a prime number.")
# else:
#     print(number, "is not a prime number.")


import math

def check_prime(n):
    if n < 2:  # Check if the number is less than 2
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Iterate from 2 to the square root of n
        if n % i == 0:  # Check if n is divisible by i
            return False  # If divisible, n is not prime
    return True  # If no divisor found, n is prime

number = int(input("Enter a number: "))  # User input for the number
is_prime = check_prime(number)
if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")





