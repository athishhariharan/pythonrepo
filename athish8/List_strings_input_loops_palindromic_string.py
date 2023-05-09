# Define a list of strings
# Loop through each string in the list
# Reverse the current string
# Check if the reversed string is the same as the original string
# If the string is a palindrome, print it
string_list = ['racecar','apple','deified','banana']
for string in string_list:
    reverse_string = string[::-1]
    if reverse_string == string:
        print(string)