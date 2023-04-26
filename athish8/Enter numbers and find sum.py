# Take input 'n' from the user to determine the numbers of integers to be added
# Initialize a variable total to 0
# Use a for loop to iterate from 1 to n(inclusive) and ask the user to input the numbers
# Add each input number to the total variable
# Print the total variable as the sum of the 'n' numbers entered by the user

n = int(input("Enter the number:"))
total = 0
for i in range(1,n):
    total += i
print(total)      