# Define a list of strings
# Initialize the variable to hold the length of the longest string
# Initialize the variable to hold the longest string
# Loop through each string in the list
# Get the length of the current string
# Check if the current string is longer than the previous longest string
# Print the longest string
string_list = ['apple', 'banana', 'cherry', 'orange', 'watermelon']
max_length = 0
longest_string = ''
for string in string_list:
    length = len(string)
    if length > max_length:
        max_length = length
        longest_string = string
print("The longest string is:", longest_string)
