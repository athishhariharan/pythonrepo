# Take a number 'n' as input
# Set a flag variable is_prime to True.
# For each integer i in the range 2 to n-1, check if n is divisible by i. If it is, set is_prime to False and exit the loop.
# If is_prime is True, print n is a prime number. Otherwise, print n is not a prime number.

n = int(input("Enter a number: "))
is_prime = True 

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")