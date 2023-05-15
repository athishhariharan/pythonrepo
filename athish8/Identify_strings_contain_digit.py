# Define a list of strings
# Loop through each string in the list
# Check if the current string contains a digit
# If it does, print the string
str_list = ["hello", "athish8", "i'm", "12"]
for string in str_list:
    if any(char.isdigit() for char in string):
        print(string)
