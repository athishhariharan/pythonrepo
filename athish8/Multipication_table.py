# Initialize a variable 'num' to 5
# Initialize for loop to iterate from 1,12
# Multiply the variable number

# Static
num = 5
for i in range(1,13):
    print(num, "x", i, "=", num * i)

# Dynamic

num = int(input("Enter a number:"))
for i in range(1,13):
    print(num, "x", i, "=", num * i)
