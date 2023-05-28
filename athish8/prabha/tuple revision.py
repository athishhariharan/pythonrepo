 # 1. Using if condition to check if an element exists in a tuple

# Tuple of fruits
fruits = ('apple', 'banana', 'orange', 'grape')

# Check if 'banana' exists in the tuple
if 'banana' in fruits:
    print('Found banana in the tuple!')
else:
    print('Did not find banana in the tuple.')

# 2. Using for loop to iterate over a tuple and print its elements

# Tuple of student names
students = ('John', 'Emily', 'Michael', 'Sarah')

# Print each student's name
for student in students:
    print(student)


# 3. Using if condition to check if an element is present in a tuple

# Define the tuple "my_tuple" with values (1, 2, 3, 4, 5).
# Use the "in" keyword to check if 3 is present in "my_tuple".
# If 3 is present in "my_tuple", print the message "3 is present in the tuple".
# Else, print the message "3 is not present in the tuple".
# Print the output message.


my_tuple = (1, 2, 3, 4, 5)

if 3 in my_tuple:
    print("3 is present in the tuple")
else:
    print("3 is not present in the tuple")
    
# Output: "3 is present in the tuple"


# 4. Using for loop to iterate over a tuple and perform some operation on each element

# Create a tuple my_tuple with values 10, 20, 30, 40, 50.
# Create an empty tuple filtered_tuple.
# Loop through each element num in the my_tuple.
# Check if the value of num is greater than 30.
# If the value of num is greater than 30, then add the value of num to the filtered_tuple.
# Print the filtered_tuple which contains only the elements greater than 30.

my_tuple = (10, 20, 30, 40, 50)

for num in my_tuple:
    print(num * 2)
    
# Output:
# 20
# 40
# 60
# 80
# 100



#5.Using while loop to iterate over a tuple and perform some operation on each element

# Initialize a tuple my_tuple with values 1, 2, 3, 4, and 5.
# Initialize a variable i with value 0.
# While i is less than the length of my_tuple, do the following:
# a. Print the square of the ith element of my_tuple.
# b. Increment i by 1.
# End the loop.

my_tuple = (1, 2, 3, 4, 5)

i = 0
while i < len(my_tuple):
    print(my_tuple[i] ** 2)
    i += 1
    
# Output:
# 1
# 4
# 9
# 16
# 25



# 6. Using if condition and for loop to filter out elements from a tuple

# Create a tuple
# Use if condition to check if an element is present in the tuple
# Use for loop to iterate over the elements of a tuple and perform some operation on each element
# Use while loop to iterate over the elements of a tuple and perform some operation on each element
# Use if condition and for loop to filter out elements from a tuple
# Print the output

my_tuple = (10, 20, 30, 40, 50)

filtered_tuple = ()
for num in my_tuple:
    if num > 30:
        filtered_tuple += (num,)

print(filtered_tuple)

# Output: (40, 50)


# 7. : Using a while loop to access elements in a tuple

# Define a tuple of student names.
# Initialize a counter variable i to 0.
# Using a while loop, iterate over the tuple until the value of i is less than the length of the tuple.
# Print the value of the tuple at the current index.
# Increment the value of i by 1.
# Repeat steps 3-5 until all elements in the tuple have been printed.

# Define a tuple of student names
students = ('Alice', 'Bob', 'Charlie', 'Dave', 'Eve')

# Use a while loop to print each student name
i = 0
while i < len(students):
    print(students[i])
    i += 1

# Output:
# Alice
# Bob
# Charlie
# Dave
# Eve


#  8. 