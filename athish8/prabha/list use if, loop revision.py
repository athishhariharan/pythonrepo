#  1. Checking if an element is in a list:
fruits = ["apple", "banana", "orange"]
if "banana" in fruits:
    print("Yes") # Output: Yes
else:
    print("No")

# 2. Counting the frequency of each element in a list:

# Create an empty dictionary called frequency.
# Loop through each element fruit in the fruits list.
# Check if the fruit is already a key in the frequency dictionary.
# If the fruit is already a key, increment its corresponding value by 1.
# If the fruit is not already a key, add it to the frequency dictionary with a value of 1.
# Print the frequency dictionary at the end.

fruits = ["apple", "banana", "cherry", "banana", "date", "apple"]
frequency = {}
for fruit in fruits:
    if fruit in frequency:
        frequency[fruit] += 1
    else:
        frequency[fruit] = 1
print(frequency) # Output: {'apple': 2, 'banana': 2, 'cherry': 1, 'date': 1}


# 3. Checking if two lists have any common elements:

# Define two lists, a and b
# Use the set() function to convert each list into a set and then use the & operator to find the intersection of the two sets, which will give a set of common elements
# Use an if statement to check if there are any common elements in the set
# If there are common elements, print them out using the print() function
# If there are no common elements, print a message indicating that the lists do not have any common elements.

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common_elements = set(a) & set(b)
if common_elements:
    print("The lists have common elements:", common_elements)
else:
    print("The lists do not have common elements")
# Output: The lists have common elements: {3, 4}

# 4. Using an if condition to filter a list of numbers:

# Create an empty list named even_numbers.
# Iterate over each element num in numbers.
# Check if num is even (i.e., num % 2 == 0).
# If num is even, append it to even_numbers.
# After iterating over all elements in numbers, print the even_numbers list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers) # Output: [2, 4, 6, 8, 10]


# 5. Using a for loop to iterate over a list of strings and extract only those that contain a certain substring:

# Create an empty list called filtered_fruits.
# Iterate through each fruit in the fruits list.
# Check if the substring "apple" is present in the current fruit using the in keyword.
# If the substring is present, append the fruit to the filtered_fruits list.
# After iterating through all the fruits in the fruits list, print the filtered_fruits list.

fruits = ["apple", "banana", "orange", "pineapple", "kiwi"]
filtered_fruits = []
for fruit in fruits:
    if "apple" in fruit:
        filtered_fruits.append(fruit)
print(filtered_fruits) # Output: ["apple", "pineapple"]

# 6. Using a while loop to remove all instances of a certain value from a list:
# Define the list of numbers.
# Check if the value 2 is present in the list.
# If it is present, remove the first occurrence of 2 from the list.
# Repeat steps 2 and 3 until all occurrences of 2 are removed from the list.
# Print the updated list without any occurrence of 2.

numbers = [1, 2, 3, 4, 5, 2, 6, 2, 7, 8, 2]
while 2 in numbers:
    numbers.remove(2)
print(numbers) # Output: [1, 3, 4, 5, 6, 7, 8]

# 7. list of numbers and we want to filter out only the even numbers

# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create an empty list to store filtered elements
even_numbers = []

# Iterate through each element in the original list
for num in numbers:
    # Check if the current element is even
    if num % 2 == 0:
        # If the element is even, add it to the filtered list
        even_numbers.append(num)

# Print the filtered list
print(even_numbers)
# Output: [2, 4, 6, 8]


# 8. Using a for loop to iterate over a list of dictionaries and extract only those that meet a certain criteria:

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 20},
    {"name": "David", "age": 30},
]

# Extract all users who are older than 25
older_users = []
for user in users:
    if user["age"] > 25:
        older_users.append(user)

print(older_users)  # Output: [{'name': 'Bob', 'age': 35}, {'name': 'David', 'age': 30}]


# 9. Using a while loop to remove duplicates from a list:

# Create an empty list called unique_numbers.
# Start a while loop that continues as long as there are items in the numbers list.
# Pop an item from the end of the numbers list and store it in a variable called num.
# Check if num is not already in the unique_numbers list using the not in operator.
# If num is not in unique_numbers, append it to unique_numbers.
# Continue the loop until all items in numbers have been checked.
# Print the unique_numbers list.

numbers = [1, 2, 3, 3, 4, 5, 5, 6, 6]
unique_numbers = []

while numbers:
    num = numbers.pop()
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)  # Output: [6, 5, 4, 3, 2, 1]


# 10. Using a for loop and an if condition to check if a list contains a certain element:

# Define a list of fruits.
# Define a variable to store the fruit we want to find.
# Use a for loop to iterate over each fruit in the list.
# Inside the for loop, check if the current fruit matches the fruit we want to find.
# If a match is found, print a message indicating that the fruit has been found and use the break statement to exit the loop.
# If the loop completes without finding a match, use the else statement to print a message indicating that the fruit was not found.

fruits = ["apple", "banana", "orange", "pineapple", "kiwi"]
fruit_to_find = "apple"

for fruit in fruits:
    if fruit == fruit_to_find:
        print("Found", fruit_to_find)
        break
else:
    print(fruit_to_find, "not found")

# Output: Found apple


# 11. Using a for loop and an if condition to filter a list of strings based on a certain condition:

# Create an empty list named filtered_sentences
# Loop through each sentence in the list sentences using a for loop
# Split the sentence into individual words using the split() method and store it in a variable named words
# Check if the length of words is greater than 3 using the len() function
# If the length of words is greater than 3, append the original sentence to the filtered_sentences list
# After all sentences have been checked, print the filtered_sentences list

sentences = ["This is a sentence", "Another sentence here", "And one more"]
filtered_sentences = []

for sentence in sentences:
    words = sentence.split()
    if len(words) > 3:
        filtered_sentences.append(sentence)

print(filtered_sentences)

# Output: ['This is a sentence', 'Another sentence here']



# 12. Using a for loop and an if condition to create a new list of tuples based on a certain condition:

# Initialize a list of numbers [1, 2, 3, 4, 5] to the variable numbers.
# Use a list comprehension to iterate over each number in the numbers list.
# Check if the current number is even using the modulo operator (num % 2 == 0).
# If the current number is even, double it and add a tuple of the original number and its doubled value to the doubled_even_numbers list.
# Print the doubled_even_numbers list.

numbers = [1, 2, 3, 4, 5]
doubled_even_numbers = []
for num in numbers:
    if num % 2 == 0:
        doubled = num * 2
        doubled_even_numbers.append((num, doubled))
print(doubled_even_numbers)

# # 13. Using a for loop and an if condition to filter out negative numbers from a list:
# 
# Initialize an empty list called positive_numbers.
# Use a for loop to iterate over each element in the numbers list.
# For each element, check if it is greater than or equal to 0 using the >= comparison operator.
# If the element is greater than or equal to 0, append it to the positive_numbers list using the append() method.
# After the loop finishes iterating over all the elements in the numbers list, print the positive_numbers list.

numbers = [-2, 3, 0, -5, 6, -1, 8]
positive_numbers = []

for num in numbers:
    if num >= 0:
        positive_numbers.append(num)

print(positive_numbers)  # Output: [3, 0, 6, 8]


# 14. Using a while loop to reverse a list:

# Define a list called fruits with four string elements.
# Define an empty list called reversed_fruits.
# Start a while loop that runs as long as the fruits list is not empty.
# Within the while loop, use the pop() method on the fruits list to remove the last element and add it to the beginning of the reversed_fruits list using the append() method.
# When the while loop is finished, print the reversed_fruits list.
# The output will show the reversed list of fruits.

fruits = ["apple", "banana", "orange", "kiwi"]
reversed_fruits = []

while fruits:
    reversed_fruits.append(fruits.pop())

print(reversed_fruits)  # Output: ['kiwi', 'orange', 'banana', 'apple']


# 15. Using a for loop and an if condition to find the longest word in a list:

# Start by initializing an empty string variable longest_word.

# Loop through each word in the list words using a for loop.

# For each word, check if its length is greater than the length of the current longest_word. If it is, update the value of longest_word to be the current word.

# Once the loop has finished, longest_word will contain the longest word in the list.

# Print the value of longest_word.

words = ["apple", "banana", "kiwi", "orange", "pineapple"]
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("The longest word is:", longest_word)  # Output: The longest word is: pineapple


# 16. Using a for loop and an if condition to count the number of occurrences of a certain element in a list:

# Initialize the list numbers.
# Initialize the variable num_to_count to the number you want to count occurrences of.
# Initialize the variable count to 0.
# Use a for loop to iterate over each element in the list numbers.
# Inside the loop, use an if condition to check if the current element is equal to num_to_count.
# If it is, increment the variable count by 1.
# After the loop, print out the number and its count.

numbers = [1, 2, 3, 2, 1, 4, 5, 1]
num_to_count = 1
count = 0
for num in numbers:
    if num == num_to_count:
         count += 1
print("The number", num_to_count, "occurs", count, "times")

# 17. Using a for loop and an if condition to flatten a list of nested lists:

# Initialize an empty list called flat_list.
# Use a for loop to iterate over each sublist in nested_list.
# Use another for loop to iterate over each number in the current sublist.
# Append each number to flat_list.
# After both loops have finished, print flat_list.

nested_list = [[1, 2], [3, 4, 5], [6, 7]]
flat_list = []

for sublist in nested_list:
    for num in sublist:
        flat_list.append(num)

print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7]


# 18. Using a for loop and an if condition to filter out duplicate elements from a list:

# Create an empty list unique_fruits.
# Iterate over each fruit in the fruits list using a for loop.
# Check if the current fruit is not already in the unique_fruits list using an if condition.
# If the fruit is not in the unique_fruits list, append it to the list.
# After iterating through all the fruits, print the unique_fruits list.

fruits = ["apple", "banana", "kiwi", "banana", "orange", "apple"]
unique_fruits = []

for fruit in fruits:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)

print(unique_fruits)  # Output: ['apple', 'banana', 'kiwi', 'orange']


# 19. Using a for loop and an if condition to find the sum of even numbers in a list:

# Initialize a list of numbers.
# Initialize a variable called even_sum to 0.
# Use a for loop to iterate over each number in the list.
# Use an if condition to check if the number is even (i.e., its remainder when divided by 2 is 0).
# If the number is even, add it to the even_sum variable.
# Print the value of the even_sum variable after the loop has finished.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num

print("Sum of even numbers:", even_sum)


# 20. Using a for loop and an if condition to find the common elements between two lists:

# Create two lists, list1 and list2, with some elements.
# Create an empty list called common_elements.
# Iterate over the elements in list1 using a for loop.
# Check if the current element is also present in list2 using the in operator.
# If the element is present in both list1 and list2, append it to the common_elements list.
# After the loop completes, print the common_elements list.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = []

for element in list1:
    if element in list2:
        common_elements.append(element)

print(common_elements)  # Output: [4, 5]


# 21. Using a while loop to remove all occurrences of a certain element from a list:

# Start by defining the list of numbers and the number to remove.
# Create a while loop that continues as long as the number to remove is in the list.
# Inside the while loop, use the remove() method of the list to remove the number to remove.
# Print the modified list outside the while loop.

numbers = [1, 2, 3, 4, 5, 2, 6, 2]
num_to_remove = 2

while num_to_remove in numbers:
    numbers.remove(num_to_remove)

print(numbers)  # Output: [1, 3, 4, 5, 6]


# 22. Using a while loop to concatenate all strings in a list:

# Initialize an empty string variable called concatenated.
# Initialize an integer variable called index to 0.
# While index is less than the length of the list words, do the following:
# a. Concatenate the current element of words and a space character to the concatenated string.
# b. Increment the index by 1.
# Remove any trailing spaces from the concatenated string using the strip() method.
# Print the concatenated string.

words = ["Hello", "world", "!", "How", "are", "you", "doing", "today?"]
concatenated = ""

index = 0
while index < len(words):
    concatenated += words[index] + " "
    index += 1

print(concatenated.strip())  # Output: Hello world ! How are you doing today?


# 23. Using a for loop and an if condition to find the sum of all odd numbers in a list:

# Create a list of numbers.
# Initialize a variable odd_sum to 0.
# Iterate over the list of numbers using a for loop.
# Check if the current number is odd using the modulus operator %. If the number is odd, add it to odd_sum.
# Print the value of odd_sum.

numbers = [2, 5, 7, 8, 9, 12, 15]
odd_sum = 0

for num in numbers:
    if num % 2 == 1:
        odd_sum += num

print("Sum of odd numbers:", odd_sum)  # Output: Sum of odd numbers: 36


#24. Finding the maximum and minimum values in a list using if conditions and for loops:

my_list = [23, 45, 11, 56, 34, 78, 90, 12, 7]

# initialize max and min variables with first element of list
max_value = my_list[0]
min_value = my_list[0]

# iterate through the list and update max and min variables accordingly
for num in my_list:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("Maximum value in the list is:", max_value)
print("Minimum value in the list is:", min_value)


# 25. Filtering out even numbers from a list using for loops and if conditions:

my_list = [23, 45, 11, 56, 34, 78, 90, 12, 7]

# initialize empty list to store even numbers
even_list = []

# iterate through the list and add even numbers to the new list
for num in my_list:
    if num % 2 == 0:
        even_list.append(num)

print("Original list:", my_list)
print("List of even numbers:", even_list)


# 26. Grocery List

grocery_list = ["apples", "bananas", "milk", "bread"]

# Print the items in the list
for item in grocery_list:
    print(item)

# 27. Student Grades

grades = [90, 85, 95, 80, 75]

# Find the average grade
total = 0
for grade in grades:
    total += grade
average = total / len(grades)
print("The average grade is:", average)


# 28. Python lists to store and manage employee details. 

employees = [
    {"name": "John", "age": 28, "salary": 50000},
    {"name": "Sarah", "age": 32, "salary": 75000},
    {"name": "Bob", "age": 45, "salary": 100000},
    {"name": "Amy", "age": 22, "salary": 40000},
]

# Print the name and salary of each employee
for employee in employees:
    print("Name:", employee["name"], "| Salary:", employee["salary"])

