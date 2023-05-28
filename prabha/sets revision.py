# 1. list of integers and we want to remove all the duplicates from it. 

# Initialize an empty set unique_numbers.
# Loop through each number in the list numbers.
# Check if the number is already in the set unique_numbers using the if condition.
# If the number is not in the set, add it to the set using the add() method.
# After the loop is done, the set unique_numbers will contain only the unique numbers from the list.
# Print the set to see the output.

numbers = [1, 2, 3, 4, 2, 5, 6, 3, 4, 5, 7]
unique_numbers = set()
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.add(num)

print(unique_numbers)


# same result using a while loop:list of integers and we want to remove all the duplicates from it


# Initialize an empty set unique_numbers.
# Initialize a counter variable i to 0.
# Use a while loop to iterate over the list numbers until i is equal to the length of numbers.
# Check if the number at index i is already in the set unique_numbers using the if condition.
# If the number is not in the set, add it to the set using the add() method.
# Increment the counter variable i.
# After the loop is done, the set unique_numbers will contain only the unique numbers from the list.
# Print the set to see the output.


numbers = [1, 2, 3, 4, 2, 5, 6, 3, 4, 5, 7]
unique_numbers = set()
i = 0
while i < len(numbers):
    if numbers[i] not in unique_numbers:
        unique_numbers.add(numbers[i])
    i += 1

print(unique_numbers)


# 2. list of numbers and we want to find the common numbers between this list and another list. 

# Create two lists of numbers.
# Convert each list to a set using the set() function.
# Create an empty list to store the common numbers.
# Loop through the first set using a for loop.
# Use an if condition to check if the current number in the first set is also in the second set.
# If it is, append the number to the list of common numbers.
# Print the list of common numbers.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

common_numbers = []

for num in set1:
    if num in set2:
        common_numbers.append(num)

print(common_numbers)


# 3. how you can use sets with if condition, for and while loops 


# Example 1: Finding common elements in sets using if condition and for loop

# Initialize two sets, set1 and set2, with some elements.
# Create an empty list called common_elements to store the common elements.
# Loop through each element in set1 using a for loop.
# Use an if condition to check if the current element is also in set2.
# If the element is in set2, append it to the common_elements list.
# Print the common_elements list.



# Example 2: Removing duplicates from a set using a while loop

# Initialize a set, set3, with some duplicate elements.
# Create an empty set called unique_elements to store the unique elements.
# Use a while loop to loop through the set3 set as long as there are elements left.
# Use the pop() method to remove an element from set3 and store it in a variable called element.
# Use an if condition to check if the element is not in the unique_elements set.
# If the element is not in unique_elements, add it to the set using the add() method.
# Continue looping through the set until all elements have been checked.
# Print the unique_elements set.



# Example 3: Filtering elements from a set using if condition and for loop

# Initialize a set, set4, with some elements.
# Create an empty set called filtered_set to store the filtered elements.
# Loop through each element in set4 using a for loop.
# Use an if condition to check if the current element is greater than 30.
# If the element is greater than 30, add it to the filtered_set set using the add() method.
# Continue looping through the set until all elements have been checked.
# Print the filtered_set set.


# Example 1: Using if condition and for loop to find common elements in sets

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

common_elements = []
for element in set1:
    if element in set2:
        common_elements.append(element)

print(common_elements)  # Output: [3, 4, 5]



# Example 2: Using while loop to remove duplicates from a set

set3 = {1, 2, 2, 3, 3, 4, 5, 5, 5}
unique_elements = set()

while set3:
    element = set3.pop()
    if element not in unique_elements:
        unique_elements.add(element)

print(unique_elements)  # Output: {1, 2, 3, 4, 5}



# Example 3: Using if condition and for loop to filter elements from a set

set4 = {10, 20, 30, 40, 50}
filtered_set = set()

for element in set4:
    if element > 30:
        filtered_set.add(element)

print(filtered_set)  # Output: {40, 50}



# 4. set and dictionary in combination with if condition, for and while loop in Python:

# Example 1: Using a dictionary to count the frequency of elements in a set


# Define a set of numbers.
# Define an empty dictionary counts.
# Iterate through the set of numbers using a for loop.
# For each number, check if it is already in the counts dictionary.
# If it is, increment its count. If it is not, add it to the counts dictionary with a count of 1.
# Print the counts dictionary.


numbers = {1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1}
counts = {}

for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

print(counts) # Output: {1: 4, 2: 3, 3: 2, 4: 1, 5: 1}


# Example 2: Using a set to remove duplicates from a list of dictionaries

# Define a list of dictionaries people.
# Define an empty set unique_people.
# Iterate through the list of dictionaries using a for loop.
# For each dictionary, create a tuple containing its 'name' and 'age' values.
# Add the tuple to the unique_people set.
# Print the unique_people set.

people = [    {'name': 'John', 'age': 30},    {'name': 'Jane', 'age': 25},    {'name': 'Bob', 'age': 30},    {'name': 'Jane', 'age': 25}]

unique_people = set()

for person in people:
    person_tuple = (person['name'], person['age'])
    unique_people.add(person_tuple)

print(unique_people) # Output: {('John', 30), ('Jane', 25), ('Bob', 30)}


# Example 3: Using a dictionary to count the frequency of words in a set of text sentences

# Define a set of text sentences.
# Define an empty dictionary word_counts.
# Iterate through the set of sentences using a for loop.
# For each sentence, split it into a list of words using the split() method.
# Iterate through the list of words using another for loop.
# For each word, check if it is already in the word_counts dictionary.
# If it is, increment its count. If it is not, add it to the word_counts dictionary with a count of 1.
# Print the word_counts dictionary.

sentences = {
    'This is a sample sentence',
    'Another sample sentence',
    'This sentence is different'
}

word_counts = {}

for sentence in sentences:
    words = sentence.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

print(word_counts) # Output: {'This': 2, 'is': 3, 'a': 2, 'sample': 2, 'sentence': 3, 'Another': 1, 'different': 1}


