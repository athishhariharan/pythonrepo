# Ask the user to enter 'n's value
# Initialize a variable 'sum' = 0.
# Use for loop to take 'n' inputs from the user and add them to 'sum'.
# Calculate the average by dividing 'sum' by 'n'.
# Print the average.

n = int(input("Enter the value of n: "))
sum = 0
for i in range(1,n):
    sum += i

average = sum / n
print("The average is", average)