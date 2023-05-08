# Define a list of strings
# Initialize the variable to hold the count of string that contain 'e'
# Loop through each string in the list
# Check if the current string contain 'e'
# Print the count of strings that contain 'e'
string_list = ['red','blue','pink','black','green']
count = 0
for string in string_list:
    if 'e' in string:
        count += 1
print(f"There are {count} strings that contain the letter'e'.")