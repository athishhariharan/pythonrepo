

# 1. if condition - making a calculator

# ask the user enter two numbers
# ask the user to choose an operation +, - , *, /
# perform the chosen operation on the two numbers
# print the result

# num1 = float(input("Enter the first number:"))
# num2 = float(input("Enter the second number:"))
# operation = input("Enter the operation(+, -, *, /):")
# if operation == "+":
#     result = num1 + num2
# elif operation == "-":
#     result = num1 - num2
# elif operation == "*":
#     result = num1 * num2
# elif operation == "/":
#     result = num1 / num2
# else:
#     print("Invalid operation")
# print("Result:", result)


# 2. check number is +, -, 0

# get the number from the user
# if the number is greater than 0, print "+"
# if the number is less than 0, print " -"
# if the number is equal to zero , print "0"

# number = float(input("Enter the number:"))
# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negative")
# else:
#     print("zero")


# 3. check if number is even or odd

# get the number from the user
# check if the number is divisible by 2 using modulo operator
# if the result of modulo operator is 0, print even
# if the result of modulo operator is 1, print odd

# number = int(input("Enter the number:"))
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")
    
# 4. largest of three numbers

# get three numbers from the user
# compare the first two numbers and find largest of the two
# compare the largest of the first two numbers with the third number and find largest of the three
# print largest number

# num1 = float(input("Enter the first number:"))
# num2 = float(input("Enter the second number:"))
# num3 = float(input("Enter the third number:"))
# if num1 >= num2 and num1 >= num3:
#     largest = num1
# elif num2 >= num1 and num2 >= num3:
#     largest = num2
# else:
#     largest = num3
# print("The largest number is:", largest)


# 5. check if given number is between 1 and 10 (inclusive)

# get the number from the user
# check if the number is greater than or equal to 1 or less than equal to 10
# if the number between 1 and 10 print "number is b/n 10"
# if the number is not b/n 1 & 10 print "number not b/n 1 & 10"

# number = int(input("Enter the number:"))
# if number >= 1 and number <= 10:
#     print("The number is between 1 and 10")
# else:
#     print("The number is not between 1 and 10")


# 6. check if a given number is odd and positive

# get the number from the user
# check if the number is odd and positive
# if the number is odd and positive, print "the number is odd and positive"
# if the number is not odd and positive print, "the number is not odd and positive"

# number = float(input(" Enter the number:"))
# if number > 0 and number % 2== 1:
#     print("The number is odd and positive")
# else:
#     print("The number is not odd and positive")


# 7. check if given string is "hello"

# get the string from the user
# check if the string is equal to "hello"
# if the string is hello print, "the string is hello"
# if the string is not hello, print " the string is not hello"

# string = input("Enter the string:")
# if string == "Hello":
#     print(" The string is Hello")
# else:
#     print("The string is not Hello")


# 8. check if given number between 1 and 10 or is negative

# get the number from the user
# check if the number is between 1 and 10 or negative
# if the number is between 1 and 10 or negative , print "the number is between 1  and 10 or nagative"


# num = int(input("Enter the number:"))
# if num <= 0 or (num >= 1 and num <= 10):
#     print("The number is between 1 and 10 or is negative")
# else:
#     print("The number is not  between 1 and 10 or is not negative")


# 9. check if given number is even and divisible by 5

# get the number from the user
# check if the number is even & divsible by 5
# if the number is even and divisible by 5, print(the number is even and divisible by 5"

# num = int(input("Enter the number:"))
# if num %2 == 0 and num % 5 == 0:
#     print("The number is even and divisible by 5")
# else:
#     print("The number is not even and not divisible by 5")

#  10. traffic signal

# signal = input("Enter the traffic signal colour:")
# if signal == "green":
#     print("go")
# elif signal == "red":
#     print("stop")
# elif signal == "orange":
#     print("wait")
# else:
#     print("invalid signal")




# 11.program that checks if Sarah can buy a new toy:

# Prompt the user to enter the price of the toy and the amount of money Sarah has.
# Convert the user input to float data type.
# Use an if-else statement to check if Sarah has enough money to buy the toy.
# If the amount of money Sarah has is greater than or equal to the price of the toy, 
# If the amount of money Sarah has is less than the price of the toy, 

# toy_price = float(input("Enter the price of the toy: "))
# sarah_money = float(input("Enter the amount of money Sarah has: "))

# if sarah_money >= toy_price:
#     print("Sarah can buy the toy.")
# else:
#     print("Sarah can't buy the toy.")



# 12. checks if Sarah is eligible for a discount:

# Prompt the user to enter Sarah's age.
# Convert the user input to integer data type.
# Use an if-else statement to check if Sarah is 12 years old or younger.
# If Sarah's age is 12 years old or younger, print a message saying she is eligible for the discount.
# If Sarah's age is older than 12, print a message saying she is not eligible for the discount.

# sarah_age = int(input("Enter Sarah's age: "))

# if sarah_age <= 12:
#     print("Sarah is eligible for the discount.")
# else:
#     print("Sarah is not eligible for the discount.")

# 13. checks if Alex passed his English exam:

# Prompt the user to enter Alex's score on the exam.
# Convert the user input to integer data type.
# Use an if-else statement to check if Alex's score is greater than or equal to 60.
# If Alex's score is greater than or equal to 60, print a message saying he passed.
# If Alex's score is less than 60, print a message saying he failed.

# alex_score = int(input("Enter Alex's score on the exam: "))

# if alex_score >= 60:
#     print("Alex passed the exam.")
# else:
#     print("Alex failed the exam.")

# 14. checks if Jack got an A in his science test:

# Prompt the user to enter Jack's science test score.
# Convert the user input to integer data type.
# Use an if-else statement to check if Jack's score is greater than or equal to 90.
# If Jack's score is greater than or equal to 90, print a message saying he got an A.
# If Jack's score is less than 90, print a message saying he didn't get an A.

# jack_score = int(input("Enter Jack's science test score: "))

# if jack_score >= 90:
#     print("Jack got an A!")
# else:
#     print("Jack didn't get an A.")


# 15. Emily wants to know if she has enough money to buy a toy.

# Get the price of the toy from the user.
# Get Emily's allowance from the user.
# If Emily's allowance is greater than or equal to the price of the toy, calculate the amount of money she will have left over by subtracting the price of the toy from her allowance.
# Display a message to Emily indicating whether or not she can afford the toy and how much money she will have left over 


# toy_price = float(input("Enter the price of the toy: "))
# allowance = float(input("Enter Emily's allowance: "))

# if allowance >= toy_price:
#     left_over = allowance - toy_price
#     print("You can buy the toy!")
#     print("You will have $", left_over, " left over.")
# else:
#     print("Sorry, you cannot afford the toy.")

# 16.  asks the user for their age and checks if they are old enough to vote.
# ask the user for their age
# Convert the user input from string to integer using the int() function
# Check if the age is greater than or equal to 18
# If the age is greater than or equal to 18, print a message saying they are old enough to vote
# if the age is less than 18, print a message saying they are not old enough to vote


# age = int(input("What is your age? "))
# if age >= 18:
#     print("You are old enough to vote.")
# else:
#     print("You are not old enough to vote.")


# 17. asks the user for two numbers and checks if the first number is divisible by the second number.

# Ask the user to enter the first number and store it in a variable
# num1 = int(input("Enter the first number: "))
 # Ask the user to enter the second number and store it in a variable
# num2 = int(input("Enter the second number: "))

# Check if the first number is divisible by the second number
# if num1 % num2 == 0:
# If the result of the modulus operator is 0, print a message saying that the first number is divisible by the second number
#     print(num1, "is divisible by", num2)
# else:
# If the result of the modulus operator is not 0, print a message saying that the first number is not divisible by the second number
#     print(num1, "is not divisible by", num2)


# 18.asks the user for a letter and checks if it is a vowel or a consonant.

# Ask user for input
# letter = input("Enter a letter: ")

#  Check if letter is a vowel or a consonant
# if letter in ['a', 'e', 'i', 'o', 'u']:
#     print(f"{letter} is a vowel")
# else:
#     print(f"{letter} is a consonant")

# 19. program that takes a number as input from the user and prints whether it is a perfect square or not.

# Take input from the user and store it in a variable.
# Find the square root of the input number using the math.sqrt() function.
# Check if the square root is an integer or not. If it is an integer, then the input number is a perfect square. Otherwise, it is not.
# Print the result accordingly.

# import math

# take input from the user
# number = int(input("Enter a number: "))

# find the square root of the input number
# sqrt = math.sqrt(number)

# check if the square root is an integer or not
# if sqrt == int(sqrt):
#     print(number, "is a perfect square.")
# else:
#     print(number, "is not a perfect square.")


# 20. program that takes a string as input and prints out whether it contains the word "python" or not:

# Get a string input from the user.
# Check if the word "python" is present in the string using the "in" keyword.
# If "python" is present, print a message saying "The string contains the word 'python'."
# If "python" is not present, print a message saying "The string does not contain the word 'python'."

# string_input = input("Enter a string: ")
# if "python" in string_input:
#     print("The string contains the word 'python'.")
# else:
#     print("The string does not contain the word 'python'.")


# 21. John wants to know if he can watch TV after finishing his homework

# Ask the user if John finished his homework.
# If the user answers "yes", print a message saying "Great job, John! You can watch TV now."
# If the user answers "no", print a message saying "You need to finish your homework .
# If the user enters anything other than "yes" or "no", print a message saying 

# homework_finished = input("Did you finish your homework? (yes/no): ")

# if homework_finished == "no":
#     print("You cannot watch TV until you finish your homework.")
# else:
#     all_homework_completed = input("Did you complete all of your homework? (yes/no): ")
#     if all_homework_completed == "no":
#         print("You cannot watch TV until you complete all of your homework.")
#     else:
#         print("You can watch TV now.")


# 22. Jack wants to know if he passed his math test. algorthim


# Ask the user for Jack's math test score and store it in a variable score.
# Check if the score is greater than or equal to 60.
# If the score is greater than or equal to 60, print a message saying "Jack passed his math test."
# Otherwise, print a message saying "Jack failed his math test.".

# Step 1
# score = input("What is Jack's math test score? ")

# Step 2
# if int(score) >= 60:
# Step 3
#     print("Jack passed his math test.")
# else:
# Step 4
#     print("Jack failed his math test.")


# asks the user for Jack's math test score and prints the corresponding letter grade:

# Ask the user to input Jack's math test score
# Convert the input score to an integer
# Use conditional statements to determine the corresponding letter grade:
# a. If the score is greater than or equal to 90, print an A
# b. If the score is between 80 and 89, print a B
# c. If the score is between 70 and 79, print a C
# d. If the score is between 60 and 69, print a D
# e. Otherwise, print an F
# End the program.

# score = int(input("Enter Jack's math test score: "))

# if score >= 90:
#     print("Jack got an A")
# elif score >= 80:
#     print("Jack got a B")
# elif score >= 70:
#     print("Jack got a C")
# elif score >= 60:
#     print("Jack got a D")
# else:
#     print("Jack got an F")

# 23. asking the user if John is in the mood for something sweet or something sour.
# Take input from the user and store it in a variable.
# Check the user's input using an if-else statement.
# If the user input is "sweet," print a message suggesting an apple.
# If the user input is "sour," print a message suggesting a grapefruit.
# If the user input is anything else, print a message suggesting a banana.

# mood = input("Is John in the mood for something sweet or something sour? ")

# if mood == "sweet":
#     print("John should have an apple for breakfast.")
# elif mood == "sour":
#     print("John should have a grapefruit for breakfast.")
# else:
#     print("John should have a banana for breakfast.")


# 24. asks the user for their age and prints a message depending on their age:

# Ask the user for their age
# age = int(input("Enter your age: "))

# Print a message depending on their age
# if age < 13:
#     print("You are a child")
# elif age >= 13 and age <= 18:
#     print("You are a teenager")
# else:
#     print("You are an adult")

# 25. ATM Withdrawal System 


# define the user's PIN and balance
# user_pin = "1234"
# user_balance = 1000.00

# ask the user for their PIN
# pin = input("Please enter your PIN: ")

# check if the PIN is correct
# if pin == user_pin:
#     # ask the user how much money they want to withdraw
#     withdrawal = float(input("How much money do you want to withdraw? "))

#  check if the user has enough balance
#     if withdrawal <= user_balance:
#  deduct the amount from the user's balance
#         user_balance -= withdrawal
#         print("You have withdrawn", withdrawal, "dollars.")
#         print("Your new balance is", user_balance, "dollars.")
#     else:
#         print("Sorry, you do not have enough balance to withdraw", withdrawal, "dollars.")
# else:
#     print("Sorry, the PIN you entered is incorrect.")


# 26. movie ticket pricing system using conditions:


# Ask the user for their age.
# Check if the user is eligible for any discounts based on their age.
# If the user is under 5 years old, print a message saying that they can watch the movie for free.
# If the user is between 5 and 12 years old, print a message saying that they need to pay $10 for a ticket.
# If the user is between 13 and 18 years old, print a message saying that they need to pay $12 for a ticket.
# If the user is over 18 years old, print a message saying that they need to pay $15 for a ticket.
# If the user enters an invalid age (e.g. a negative number), print an error message.

# age = int(input("Enter your age: "))

# if age < 0:
#     print("Invalid age.")
# elif age < 5:
#     print("You can watch the movie for free.")
# elif age <= 12:
#     print("You need to pay $10 for a ticket.")
# elif age <= 18:
#     print("You need to pay $12 for a ticket.")
# else:
#     print("You need to pay $15 for a ticket.")


# 27. Online Shopping Discount System:


# Ask the user to enter the total amount of their purchase
# Check if the total amount is greater than or equal to $100. If it is, apply a 10% discount. If not, do not apply any discount.
# Display the final amount to be paid after the discount.

# total_amount = float(input("Enter the total amount of your purchase: "))

# if total_amount >= 100:
#     discount = 0.1 * total_amount
#     final_amount = total_amount - discount
#     print("You have received a discount of $", discount)
#     print("Your final amount is $", final_amount)
# else:
#     print("Your final amount is $", total_amount)


# 28. car Rental Pricing System:


# Ask the user how many days they want to rent the car for
# Check if the number of days is greater than or equal to 7. If it is, apply a discount of 10% on the total rental cost. If not, do not apply any discount.
# Display the final rental cost to the user.

# rental_days = int(input("How many days do you want to rent the car for? "))
# daily_rental_cost = 50
# total_rental_cost = rental_days * daily_rental_cost

# if rental_days >= 7:
#     discount = 0.1 * total_rental_cost
#     final_rental_cost = total_rental_cost - discount
#     print("You have received a discount of $", discount)
#     print("Your final rental cost is $", final_rental_cost)
# else:
#     print("Your rental cost is $", total_rental_cost)

# 
#29.  Meal Pricing System:

# Take user input for their order.
# Calculate the price of the order depending on the items and quantity.
# Check if the user is eligible for any discounts based on the total price of their order.
# Apply the discount if applicable.
# Print the final price of the order.

# order = input("Enter your order: ")
# quantity = int(input("Enter quantity: "))
# price = 0

# if order == "burger":
#     price = 2.50
# elif order == "fries":
#     price = 1.50
# elif order == "drink":
#     price = 1.00

# total_price = price * quantity

# if total_price >= 5.00:
#     total_price *= 0.9

# print("Total price: $", total_price)


# 30. School Grade Calculation:

# Take user input for their marks in three subjects.
# Calculate the average marks.
# Check the grade based on the average marks using an if-elif statement.
# Print the grade.

# subject1 = float(input("Enter marks for subject 1: "))
# subject2 = float(input("Enter marks for subject 2: "))
# subject3 = float(input("Enter marks for subject 3: "))

# average_marks = (subject1 + subject2 + subject3) / 3

# if average_marks >= 90:
#     grade = "A+"
# elif average_marks >= 80:
#     grade = "A"
# elif average_marks >= 70:
#     grade = "B"
# elif average_marks >= 60:
#     grade = "C"
# elif average_marks >= 50:
#     grade = "D"
# else:
#     grade = "F"

# print("Your grade is:", grade)


# 31. Delivery System:

# Ask the user for their location and order value.
# If the user's location is within the delivery area and their order value is greater than or equal to $20, print "Your order will be delivered".
# If the user's location is within the delivery area but their order value is less than $20, print "Your order does not meet the minimum value for delivery".
# If the user's location is outside the delivery area, print "Delivery is not available in your area".

# location = input("Enter your location: ")
# order_value = float(input("Enter your order value: "))
# if location == "XYZ" and order_value >= 20:
#     print("Your order will be delivered.")
# elif location == "XYZ" and order_value < 20:
#     print("Your order does not meet the minimum value for delivery.")
# else:
#     print("Delivery is not available in your area.")



# 32. scholarship System:


# Ask the user for their academic score.
# If the user's score is greater than or equal to 90%, print "You are eligible for a full scholarship".
# If the user's score is between 80% and 89%, print "You are eligible for a half scholarship".
# If the user's score is less than 80%, print "You are not eligible for a scholarship".

# score = float(input("Enter your academic score: "))
# if score >= 90:
#     print("You are eligible for a full scholarship.")
# elif score >= 80 and score < 90:
#     print("You are eligible for a half scholarship.")
# else:
#     print("You are not eligible for a scholarship.")


# 33. Age-based Ticket Pricing System for a Theme Park:

# Take the age of the user as input.
# Check if the user is below 5 years of age.
# If yes, print "Admission is free for children below 5 years".
# If no, check if the user is between 5 and 12 years of age.
# If yes, print "Admission fee is $10 for children between 5 and 12 years".
# If no, check if the user is between 13 and 59 years of age.
# If yes, print "Admission fee is $15 for adults between 13 and 59 years".
# If no, print "Admission fee is $10 for senior citizens above 60 years".

# age = int(input("Enter your age: "))
# if age < 5:
#     print("Admission is free for children below 5 years")
# elif age >= 5 and age <= 12:
#     print("Admission fee is $10 for children between 5 and 12 years")
# elif age >= 13 and age <= 59:
#     print("Admission fee is $15 for adults between 13 and 59 years")
# else:
#     print("Admission fee is $10 for senior citizens above 60 years")


# 34.  Admission eligibility check:

# Ask the user to enter their age and the minimum age requirement for admission.
# If the user's age is less than the minimum age requirement, display a message indicating they are not eligible for admission.
# If the user's age is greater than or equal to the minimum age requirement, display a message indicating they are eligible for admission.

# age = int(input("Enter your age: "))
# min_age = 18
# if age < min_age:
#     print("You are not eligible for admission.")
# else:
#     print("You are eligible for admission.")


# 35. Discount calculation:

# Ask the user to enter the price of an item and their membership status.
# If the user is a member, apply a discount of 10% and calculate the final price.
# If the user is not a member, do not apply a discount and calculate the final price.

# price = float(input("Enter the price of the item: "))
# is_member = input("Are you a member? (yes or no): ")
# if is_member == "yes":
#     discount = 0.1
# else:
#     discount = 0
# final_price = price * (1 - discount)
# print("The final price is:", final_price)



# 36. Weather Forecasting System:


# Get the user input for the temperature.
# Check if the temperature is less than or equal to 32 degrees Fahrenheit.
# If the temperature is less than or equal to 32 degrees Fahrenheit, print "It's freezing outside, wear a jacket!"
# If the temperature is between 32 and 70 degrees Fahrenheit, print "It's cool outside, wear a light jacket!"
# If the temperature is between 70 and 90 degrees Fahrenheit, print "It's warm outside, wear shorts and a t-shirt!"
# If the temperature is above 90 degrees Fahrenheit, print "It's hot outside, stay cool and hydrated!"

# temperature = float(input("Enter the temperature in Fahrenheit: "))

# if temperature <= 32:
#     print("It's freezing outside, wear a jacket!")
# elif temperature > 32 and temperature <= 70:
#     print("It's cool outside, wear a light jacket!")
# elif temperature > 70 and temperature <= 90:
#     print("It's warm outside, wear shorts and a t-shirt!")
# else:
#     print("It's hot outside, stay cool and hydrated!")



 
# 37. asks the user for their monthly income and expenses, calculates their monthly budget, and provides some suggestions based on the budget:

# Ask for user input
# income = float(input("Enter your monthly income: "))
# expenses = float(input("Enter your monthly expenses: "))

# Calculate budget
# budget = income - expenses

# Print budget and suggestions
# print("Your monthly budget is $", budget)

# if budget > 0:
#     print("You have a surplus in your budget. Consider saving or investing this extra money.")
# elif budget < 0:
#     print("You have a deficit in your budget. Consider reducing expenses or finding additional sources of income.")
# else:
#     print("Your income and expenses are balanced. Keep up the good work!")
