
# 1. printout the numbers from 1 to 10

# use for loop to iterate through numbers from 1 to 10
# print out each number

# for i in range(1,11):
#     print(i)


# 2. print out the even numbers from 1 to 20

# use for loop to iterate through the numbers from 1 to 20
# check if the current number is even
# if it is even, print out the number

# for number in range(1,21):
#     if number % 2 == 0: 
#         print(number)


# 3. calculate sum of first 10 numbers

# set variable total to 0
# use for loop to iterate through the numbers from 1 to 10
# add each number to the  total variable
# print out the total variable

# total = 0
# for number in range(1,11):
#     total += number
# print("The sum of first 10 numbers is:", total)

# list of numbers assigned

# numbers = [1,2,3,7,8,9]
# sum = 0
# for num in numbers:
#     sum += num
# print(sum)


# 4. To calculate the factorial of a number

# initialize a variable 'n' number to calculate factorial of 5
# initialize a variable 'factorial' to 1
# loop from 1 to n
# multiply 'factorial' by each number from 1 to n
# print result

# n = 5
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print(factorial)

# or

# n = int(input("Enter a number:"))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print("The factorial of", n, "is", factorial)


# 5. program accepts a string and print total number of vowels in the string

# initialize a variable 'string' with some string value
# initialize a variable 'vowels' to a list of vowels
# initialize a variable count 0
# loop through each character in the string
# if the character is a vowel, increment the 'count' variable
# print 'count' variable

# string = "Hello World"
# vowels = ['a', 'e', 'i', 'o', 'u']
# count = 0
# for char in string.lower():
#     if char in vowels:
#         count += 1
# print(count)
    
# if vowels to be remove

# string = "Hello World"
# vowels = ['a', 'e', 'i', 'o', 'u']
# count = ""
# for char in string.lower():
#     if char not in vowels:
#        count += char
# print(count)

# 6. # 2.multiplication table

# get the nuber from the user
# convert the input to an integer & store it in a variable
# initialize a loop to iterate from 1 to 10
# multiply the input number

# number = input("Enter a number:")
# number = int(number)
# for i in range(1,11):
#     result = number * i
#     print(number, "x", i, "=", result)

# 7. sum of all even numbers from 1 to 10 using a for loop:

# Initialize a variable sum to 0.
# Use a for loop to iterate over the range of numbers from 1 to 10.
# For each number in the range, check if it is even by using the modulus operator %. If the number is even, add it to the sum variable.
# After the loop has finished, print the value of sum

# sum = 0

# for num in range(1, 11):
#     if num % 2 == 0:
#         sum += num

# print(sum)

# 8.reversing the order of elements in a list using a for loop:

# Create a list of numbers.
# Initialize an empty list called reversed_list.
# Use a for loop to iterate over the original list in reverse order.
# For each number in the original list, append it to the reversed_list.
# After the loop has finished, print the reversed_list.

# numbers = [1, 2, 3, 4, 5]
# reversed_list = []

# for i in range(len(numbers)-1, -1, -1):
#     reversed_list.append(numbers[i])

# print(reversed_list)


 
# 9.checks if a given number is prime or not can be implemented using a loop.


# Take a number n as input.
# Set a flag variable is_prime to True.
# For each integer i in the range 2 to n-1, check if n is divisible by i. If it is, set is_prime to False and exit the loop.
# If is_prime is True, print n is a prime number. Otherwise, print n is not a prime number.

# n = int(input("Enter a number: "))
# is_prime = True

# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")


# 10. program that asks the user to enter n numbers and calculates their sum:


# Take input 'n' from the user to determine the number of integers to be added
# Initialize a variable total to 0
# Use a for loop to iterate from 1 to n (inclusive) and ask the user to input the numbers
# Add each input number to the total variable
# Print the total variable as the sum of the n numbers entered by the user.

# n = int(input("Enter the number of integers to add: "))
# total = 0
# for i in range(1, n+1):
#     num = int(input(f"Enter number {i}: "))
#     total += num
# print(f"The sum of the {n} numbers is: {total}")


# 11. Finding the average of n numbers

# Ask the user to enter the value of n.
# Initialize a variable 'sum' to 0.
# Use a for loop to take n inputs from the user and add them to 'sum'.
# Calculate the average by dividing 'sum' by n.
# Print the average.

# n = int(input("Enter the value of n: "))
# sum = 0

# for i in range(n):
#     num = float(input("Enter a number: "))
#     sum += num

# average = sum / n
# print("The average is", average)

# 12. Finding the maximum of n numbers
# 

# Ask the user to enter the value of n.
# Initialize a variable 'max_num' to -infinity.
# Use a for loop to take n inputs from the user and compare them with 'max_num'.
# If the input number is greater than 'max_num', update 'max_num'.
# Print the maximum number.

# n = int(input("Enter the value of n: "))
# max_num = -float('inf')

# for i in range(n):
#     num = float(input("Enter a number: "))
#     if num > max_num:
#         max_num = num

# print("The maximum number is", max_num)


# 13. Finding the minimum of n numbers


# Ask the user to enter the value of n.
# Initialize a variable 'min_num' to infinity.
# Use a for loop to take n inputs from the user and compare them with 'min_num'.
# If the input number is less than 'min_num', update 'min_num'.
# Print the minimum number.

n = int(input("Enter the value of n: "))
min_num = float('inf')

for i in range(n):
    num = float(input("Enter a number: "))
    if num < min_num:
        min_num = num

print("The minimum number is", min_num)




 # 14. for loop to calculate monthly expenses and income for a user:




# Ask the user for the number of expenses and income sources they have
# num_expenses = int(input("Enter the number of monthly expenses: "))
# num_income = int(input("Enter the number of monthly income sources: "))

# Initialize variables for the total expenses and income
# total_expenses = 0
# total_income = 0

#  Loop through each expense and add it to the total
# for i in range(num_expenses):
#     expense = float(input("Enter the amount of expense " + str(i+1) + ": "))
#     total_expenses += expense

# Loop through each income source and add it to the total
# for i in range(num_income):
#     income = float(input("Enter the amount of income " + str(i+1) + ": "))
#     total_income += income

# Calculate the difference between income and expenses
# savings = total_income - total_expenses

# Print the total expenses, income, and savings for the month
# print("Total monthly expenses: $", format(total_expenses, '.2f'))
# print("Total monthly income: $", format(total_income, '.2f'))
# print("Savings for the month: $", format(savings, '.2f'))


 
# 15. asks the user for their monthly income and expenses and calculates their monthly budget 


#  Ask the user for their monthly income
# monthly_income = float(input("Enter your monthly income: "))

#  Ask the user for their monthly expenses
# num_expenses = int(input("How many monthly expenses do you have? "))
# monthly_expenses = 0
# for i in range(num_expenses):
#     expense = float(input("Enter expense amount: "))
#     monthly_expenses += expense

#  Calculate the monthly budget
# monthly_budget = monthly_income - monthly_expenses

# Print the monthly budget
# print("Your monthly budget is: $", monthly_budget)

