# 1. print numbers from 1 to 10

# set a variable called number to 1
# create a while loop that runs as long as number is >= to 10
# inside the while loop, print out the value of number
# increment the value of number by 1
# end the while loop

# number = 1
# while number <= 10:
#     print(number)
#     number += 1


 # 2. print numbers from 10 to 1
# Initialize a variable num to 10.
# While num is greater than or equal to 1, do the following:
# a. Print the value of num.
# b. Decrement the value of num by 1.

# num = 10
# while num >= 1:
#     print(num)
#     num -= 1


# 3. Password Authentication

# Ask the user to enter their password.
# Initialize a variable attempts to 0.
# While the user's password is not correct and attempts is less than 3, do the following:
# a. Ask the user to enter their password again.
# b. Increment the attempts variable by 1.
# If the user enters the correct password, print "Access granted!".
# If the user enters an incorrect password 3 times, print "Access denied." and exit the program.

# password = "my_password"
# attempts = 0

# while password != input("Enter your password: ") and attempts < 2:
#     attempts += 1

# if attempts == 2:
#     print("Access denied.")
# else:
#     print("Access granted!")


# 4. Countdown Timer


# Ask the user to enter the number of seconds for the timer.
# Initialize a variable time_left to the number of seconds entered by the user.
# While time_left is greater than 0, do the following:
# a. Print the value of time_left.
# b. Decrement the value of time_left by 1.
# c. Pause the program for 1 second.
# When time_left reaches 0, print "Time's up!" and exit the program.


# import time

# time_left = int(input("Enter the number of seconds: "))

# while time_left > 0:
#     print(time_left)
#     time_left -= 1
#     time.sleep(1)

# print("Time's up!")


# 5. Generating a Fibonacci Sequence


# Initialize variables a and b to 0 and 1, respectively.
# While b is less than or equal to a certain limit, do the following:
# a. Print the value of b.
# b. Set a equal to b and b equal to a + b.

# a, b = 0, 1
# limit = 50

# while b <= limit:
#     print(b)
#     a, b = b, a + b

# 6. Initialize a variable password with a value of "password123".
# Prompt the user to enter a password.
# While the password entered by the user is not equal to the correct password, do the following:
# a. Print a message indicating that the password is incorrect.
# b. Prompt the user to enter a password again.
# Print a message indicating that the password is correct.

# password = "password123"

# while True:
#     user_password = input("Enter the password: ")
#     if user_password == password:
#         print("Password is correct!")
#         break
#     else:
#         print("Incorrect password, please try again.")


# 7. program that uses a while loop to print the first 5 multiples of 3:


# Initialize a variable count to 0.
# While count is less than 5, do the following:
# a. Calculate the next multiple of 3 by multiplying count by 3.
# b. Print the result.
# c. Increment count by 1.

# count = 0

# while count < 5:
#     multiple = (count + 1) * 3
#     print(multiple)
#     count += 1


# 8. print the squares of the numbers from 1 to 5:


# Initialize a variable count to 1.
# While count is less than or equal to 5, do the following:
# a. Calculate the square of the current value of count.
# b. Print the result.
# c. Increment count by 1.

# count = 1

# while count <= 5:
#     square = count ** 2
#     print(square)
#     count += 1

# 9. add numbers to a list until the sum of the list is greater than 100:


# Initialize a variable total to 0.
# Initialize an empty list called numbers.
# While total is less than or equal to 100, do the following:
# a. Prompt the user to enter a number.
# b. Convert the input to an integer and append it to the numbers list.
# c. Add the new number to the total.
# Print the numbers list.

# total = 0
# numbers = []

# while total <= 100:
#     num = int(input("Enter a number: "))
#     numbers.append(num)
#     total += num

# print("The numbers that were entered are:", numbers)


# 10. to calculate the sum of all numbers from 1 to 100:

# Initialize a variable count to 1.
# Initialize a variable total to 0.
# While count is less than or equal to 100, do the following:
# a. Add count to the total.
# b. Increment count by 1.
# Print the value of total.

# count = 1
# total = 0

# while count <= 100:
#     total += count
#     count += 1

# print("The sum of all numbers from 1 to 100 is:", total)

# 11. to print out the first 5 even numbers:

# Initialize the variable to keep track of the loop's progress
# num = 0

# Write the while loop with the appropriate condition
# while num < 10:

# Write the code to be executed inside the loop
#     print(num)

# Update the variable to move the loop towards completion
#     num += 2


# 12. asks the user to enter n numbers and calculates their sum and average using a while loop:

 # Ask the user to enter the value of n
# n = int(input("Enter the value of n: "))

# Initialize variables for sum and count
# sum = 0
# count = 0

# Loop n times to get the numbers from the user
# while count < n:
#     num = float(input("Enter a number: "))
#     sum += num
#     count += 1

# Calculate the average
# avg = sum / n

# Print the sum and average
# print("The sum of the numbers is:", sum)
# print("The average of the numbers is:", avg)

# 13. asks the user to enter n numbers using a while loop and calculates their sum:

# Ask the user to enter the value of n
# Initialize a variable sum to 0
# Initialize a counter variable count to 1
# Use a while loop to iterate from 1 to n
# Within the loop, ask the user to enter a number and add it to the sum
# Increment the value of count
# After the loop, print the sum of the n numbers entered by the user

# n = int(input("Enter the value of n: "))
# sum = 0
# count = 1

# while count <= n:
#     num = int(input("Enter a number: "))
#     sum += num
#     count += 1

# print("The sum of the entered numbers is:", sum)



 # 14. calculates grades, percentages, and averages using both while loop

# initialize variables
# total_marks = 0
# num_subjects = 0

# use while loop to get input from user
# while True:
#     marks = input("Enter marks for subject (or 'done' to finish): ")
#     if marks == 'done':
#         break
#     else:
#         marks = int(marks)
#         total_marks += marks
#         num_subjects += 1

# calculate percentage and average
# percentage = (total_marks / (num_subjects * 100)) * 100
# average = total_marks / num_subjects

# print results
# print("Total marks: ", total_marks)
# print("Number of subjects: ", num_subjects)
# print("Percentage: ", percentage)
# print("Average: ", average)



# 15. A user wants to calculate their monthly expenses and income to determine how much they can save each month.


# Initialize the variable total_expenses to 0 and total_income to 0.
# Use a while loop to repeatedly ask the user for their expenses and income until they enter "done".
# For each expense, add it to total_expenses.
# For each income, add it to total_income.
# After the loop has finished, calculate the difference between total_income and total_expenses to determine the monthly savings.
# Print the total expenses, total income, and monthly savings.

# total_expenses = 0
# total_income = 0

# while True:
#     expense_or_income = input("Enter expense or income (type 'done' to finish): ")
    
#     if expense_or_income == "done":
#         break
    
#     amount = float(input("Enter amount: "))
    
#     if expense_or_income == "expense":
#         total_expenses += amount
#     elif expense_or_income == "income":
#         total_income += amount

# monthly_savings = total_income - total_expenses

# print("Total expenses:", total_expenses)
# print("Total income:", total_income)
# print("Monthly savings:", monthly_savings)



# 16. asks the user for their monthly income and expenses and calculates their monthly budget:


# Initialize variables
# income = 0
# expenses = 0
# total_expenses = 0

# Get income from user
# income = float(input("Enter your monthly income: "))

# Get expenses from user using a while loop
# while True:
#     expense = input("Enter an expense name (or 'done' to finish): ")
#     if expense.lower() == 'done':
#         break
#     cost = float(input("Enter the expense cost: "))
#     expenses += cost

# Calculate total expenses
# total_expenses = expenses

# # Calculate monthly budget
# budget = income - total_expenses

# Display results to user
# print("Monthly Income: $", format(income, ".2f"))
# print("Monthly Expenses: $", format(total_expenses, ".2f"))
# print("Monthly Budget: $", format(budget, ".2f"))

# Determine if budget is positive or negative and provide feedback to user
# if budget > 0:
#     print("Congratulations! You have a surplus this month.")
# elif budget == 0:
#     print("Your budget is balanced this month.")
# else:
#     print("Be careful, you are in a deficit this month.")



