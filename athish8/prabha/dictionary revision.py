# 1. Counting Occurrences of Words in a Text

# Create a variable text and assign it a string value.
# Create an empty dictionary word_counts to store the count of each word.
# Split the text into words using the split() method, and iterate over each word in the resulting list.
# For each word:
# a. Check if it is already a key in word_counts by using the in operator.
# b. If the word is a key in word_counts, increment its value by 1.
# c. If the word is not a key in word_counts, add it as a key with a value of 1.
# Print the word_counts dictionary.

text = "This is a sample text with several words. This is another sample text with some more words."

word_counts = {}
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)


# 2. Counting Unique Items in a List


# Create a list items with multiple values, some of which are repeated.
# Create an empty dictionary item_counts to store the count of each item.
# Iterate over each item in the items list.
# For each item:
# a. Check if it is already a key in item_counts by using the in operator.
# b. If the item is a key in item_counts, increment its value by 1.
# c. If the item is not a key in item_counts, add it as a key with a value of 1.
# Print the item_counts dictionary.

items = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana', 'banana']

item_counts = {}
for item in items:
    if item in item_counts:
        item_counts[item] += 1
    else:
        item_counts[item] = 1

print(item_counts)




# 3. Word Frequency Counter

# Create a variable text and assign it a string value.
# Split the text into words using the split() method and assign it to the variable words.
# Create an empty dictionary word_counts to store the count of each word.
# Iterate over each word in the words list.
# For each word:
# a. Check if it is already a key in word_counts by using the in operator.
# b. If the word is a key in word_counts, increment its value by 1.
# c. If the word is not a key in word_counts, add it as a key with a value of 1.
# Print the word_counts dictionary.

text = "The quick brown fox jumps over the lazy dog"
words = text.split()

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)


# 4. Contact List

# Create a dictionary contacts with three key-value pairs.
# Each key is a string representing a contact's name, and each value is another dictionary.
# The nested dictionaries contain two key-value pairs: 'email' and 'phone'.
# The values for 'email' and 'phone' are strings representing the contact's email address and phone number, respectively.
# Use indexing to access the value of the 'email' key for the 'John' contact in the contacts dictionary.
# Print the value of 'email' for the 'John' contact.

contacts = {
    'John': {'email': 'john@example.com', 'phone': '123-456-7890'},
    'Jane': {'email': 'jane@example.com', 'phone': '234-567-8901'},
    'Bob': {'email': 'bob@example.com', 'phone': '345-678-9012'}
}

print(contacts['John']['email'])  # Output: john@example.com



# 5. Sales Report

# Create a dictionary sales_data with five key-value pairs.
# Each key is a string representing a product, and each value is an integer representing the quantity sold.
# Use the sum() function with the values() method to calculate the total sales from the sales_data dictionary.
# Store the result in the variable total_sales.
# Create an empty list top_selling_products to store the names of the top-selling products.
# Iterate over each product and quantity pair in the sales_data dictionary using the items() method.
# For each product and quantity pair:
# a. Check if the quantity is greater than or equal to 30.
# b. If the quantity is greater than or equal to 30, append the product to the top_selling_products list.
# Use the join() method with the ', ' separator to convert the top_selling_products list into a string and print it.
# Print the total sales.
# 


sales_data = {
    'apple': 10,
    'banana': 20,
    'orange': 30,
    'grape': 40,
    'watermelon': 50
}

total_sales = sum(sales_data.values())
print('Total sales: {}'.format(total_sales))

top_selling_products = []
for product, quantity in sales_data.items():
    if quantity >= 30:
        top_selling_products.append(product)

print('Top selling products: {}'.format(', '.join(top_selling_products)))


# 6. User Input Validation

# Create a dictionary allowed_values with two keys: 'color' and 'size', and the corresponding values as lists of allowed values for each field.
# Create an empty dictionary user_input.
# For each field and allowed list in the allowed_values dictionary, do the following:
# a. Start an infinite loop using the while True statement.
# b. Ask the user to input a value for the field using the input() function and store it in the variable value.
# c. Check if the value entered by the user is in the allowed list using the in operator.
# d. If the value is in the allowed list, store it in the user_input dictionary with the field as the key and the value as the value, and break out of the loop using the break statement.
# e. If the value is not in the allowed list, print an error message telling the user that the value is invalid and display the allowed values using the join() method with the ', ' separator.
# After the loop, print the user_input dictionary.


allowed_values = {
    'color': ['red', 'green', 'blue'],
    'size': ['small', 'medium', 'large']
}

user_input = {}
for field, allowed in allowed_values.items():
    while True:
        value = input('Enter {}: '.format(field))
        if value in allowed:
            user_input[field] = value
            break
        else:
            print('Invalid value. Allowed values: {}'.format(', '.join(allowed)))

print('User input: {}'.format(user_input))

# 7. 