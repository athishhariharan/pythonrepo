# Initialize the sum to 0
# Loop over the range of numbers from 1 to 100
# Check if the number is a multiple of 3
# If it is,skip to the next iteration
# If it's not a multiple of 3, add it to the sumPrint
# Print the final sum
sum = 0
for i in range(1,101):
    if i % 3 == 0:
        continue
    sum += i
    print("The sum of all numbers from 1 to 100, skipping multiples of 3, is:", sum)