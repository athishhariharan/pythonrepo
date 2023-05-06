# Take input from the user
# Loop from 1 to 10
# Multiply the number with a loop variable
# Check if the result is even
# If it's even, skip to the next iteration
# Print the result if it's not even
num = int(input("Enter a number:"))
for i in range(1,11):
    result = num * i
    if result % 2 == 0:
        continue
    print(f"{num} x {i} = {result}")