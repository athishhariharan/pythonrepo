# Set a variable 'sum' to 0.
# Use for loop to iterate the range of numbers from 1 to 10.
# For each number in the range, check if it's even by using modulus operator %. If the number's even, add it to the sum.
# After the loop has finished, print the value of sum

sum = 0

for num in range(1, 11):
    if num % 2 == 0:
         sum += num

print(sum)
