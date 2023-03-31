# 1.  the user to enter a string and converts it to uppercase:

# Prompt the user to enter a string and store the input in a variable called string.
# Use the upper() method to convert the string to uppercase and store the result in a variable called uppercase_string.
# Print the original string and the uppercase string using the print() function.

string = input("Enter a string: ")

# Using the upper() method to convert the string to uppercase
uppercase_string = string.upper()

print("Original String: ", string)
print("Uppercase String: ", uppercase_string)


# 2. program that counts the number of words in a sentence:

# Algorithm:

# Define the sentence as a string and store it in a variable called sentence.
# Use the split() method to split the sentence into words and store the result in a list called words.
# Count the number of words in the list using the len() function and store the result in a variable called num_words.
# Print the number of words in the sentence using the print() function.

sentence = "the quick brown fox jumps"

# Using the split() method to split the sentence into words
words = sentence.split()

# Counting the number of words in the list
num_words = len(words)

print("Number of words in the sentence: ", num_words)


# 3. counts the number of vowels in a string:

# Prompt the user to enter a string using the input() function and store the result in a variable called string.
# Define a set of vowels using the set() function and store the result in a variable called vowels.
# Initialize a count variable to 0.
# Loop through each character in the string using a for loop.
# Check if the character is a vowel by using the in operator to check if it's in the set of vowels.
# If the character is a vowel, increment the count variable by 1.
# After looping through all the characters in the string, print the count using the print() function.

string = input("Enter a string: ")

# Defining a set of vowels
vowels = set("aeiouAEIOU")

# Initializing the count to 0
count = 0

# Looping through each character in the string
for char in string:
    # Checking if the character is a vowel
    if char in vowels:
        count += 1

print("Number of vowels in the string: ", count)


# 4.  reversing a string using string manipulation:

# Algorithm:

# Prompt the user to enter a string using the input() function and store the result in a variable called string.
# Use the slice notation [::-1] to reverse the string and store the result in a new variable called reversed_string.
# Print the reversed_string variable using the print() function.

string = input("Enter a string: ")

# Using slice notation to reverse the string
reversed_string = string[::-1]

print("Reversed string: ", reversed_string)


# 5. program that demonstrates how to find the repeated words in a string using split() and set():

# Real-life scenario: finding repeated words in a string
string = "The quick brown fox jumps over the lazy dog and the quick brown fox jumps over the lazy dog again."

# Splitting the string into words using split() method
words = string.split()

# Creating a set of unique words in the string
unique_words = set(words)

# Initializing a list to store the repeated words
repeated_words = []

# Looping through the unique words and checking if they appear more than once in the original string
for word in unique_words:
    if words.count(word) > 1:
        repeated_words.append(word)

# Printing the repeated words
print("The repeated words in the string are:")
for word in repeated_words:
    print(word)


# 6. counts the occurrence of each letter in the string and updates the dictionary with the count:

# Defining a string
string = "Hello World"

# Initializing an empty dictionary
dictionary = {}

# Looping through each character in the string
for char in string:
    # Updating the count of the character in the dictionary
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

# Printing the string and the dictionary
print("String:", string)
print("Dictionary:", dictionary)


# 7. len(): This function returns the length of a string

# Accepting input from the user
string = input("Enter a string: ")

# Getting the length of the string
length = len(string)

# Displaying the length of the string
print("The length of the string is:", length)


# 8. upper(): This function returns a copy of the string with all the characters in uppercase.

# Accepting input from the user
string = input("Enter a string: ")

# Converting the string to uppercase
uppercase_string = string.upper()

# Displaying the uppercase string
print("Uppercase string:", uppercase_string)


# 9. lower(): This function returns a copy of the string with all the characters in lowercase.

# Accepting input from the user
string = input("Enter a string: ")

# Converting the string to lowercase
lowercase_string = string.lower()

# Displaying the lowercase string
print("Lowercase string:", lowercase_string)


# 10. strip(): This function removes any leading and trailing whitespace characters from the string.

# Accepting input from the user
string = input("Enter a string: ")

# Removing leading and trailing whitespace characters
stripped_string = string.strip()

# Displaying the stripped string
print("Stripped string:", stripped_string)


# 11. split(): This function splits the string into a list of substrings based on the specified separator.

# Accepting input from the user
string = input("Enter a string: ")

# Splitting the string into a list of substrings
substrings = string.split()

# Displaying the list of substrings
print("List of substrings:", substrings)



# 11. join(): This function joins the elements of a list into a single string using the specified separator.

# Define a list of strings
words = ['hello', 'world', 'how', 'are', 'you']

# Define the separator
separator = ' '

# Join the strings using the separator
result = separator.join(words)

# Print the resulting string
print(result)


# 12.append(): This function is used to add an element to the end of a list.

# Create a list
my_list = [1, 2, 3, 4, 5]

# Add an element to the end of the list
my_list.append(6)

# Print the updated list
print(my_list)


#13. index(): This function is used to find the index of the first occurrence of an element in a list.

# Create a list
my_list = ['apple', 'banana', 'cherry', 'banana', 'orange']

# Find the index of the first occurrence of 'banana'
index = my_list.index('banana')

# Print the index
print(index)


# 14.insert(): This function is used to add an element to a list at a specific position.

# Create a list
my_list = [1, 2, 3, 4, 5]

# Add the number 0 to the beginning of the list
my_list.insert(0, 0)

# Print the updated list
print(my_list)


# 15. remove(): This function is used to remove the first occurrence of an element from a list.

# Create a list
my_list = ['apple', 'banana', 'cherry', 'orange']

# Remove 'banana' from the list
my_list.remove('banana')

# Print the updated list
print(my_list)


# 16. sort(): This function is used to sort the elements of a list in ascending order.

# Create a list
my_list = [3, 2, 4, 1, 5]

# Sort the list in ascending order
my_list.sort()

# Print the sorted list
print(my_list)

# 17. reverse(): This function is used to reverse the order of the elements in a list.

# Create a list
my_list = [1, 2, 3, 4, 5]

# Reverse the order of the elements in the list
my_list.reverse()

# Print



# 18. pop(): This function removes and returns the element at the specified index of the list. If no index is specified, it removes and returns the last element of the list


fruits = ['apple', 'banana', 'cherry']
removed_fruit = fruits.pop(1)
print(fruits) # Output: ['apple', 'cherry']
print(removed_fruit) # Output: 'banana'


# 19. count(): This function returns the number of times the specified element appears in the list.

numbers = [1, 2, 3, 4, 5, 2, 2]
count_of_twos = numbers.count(2)
print(count_of_twos) # Output: 3


