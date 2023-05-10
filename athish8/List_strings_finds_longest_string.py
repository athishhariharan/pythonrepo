# Define a list of strings
# Initialize a variable to hold the longest string
# Loop through each string in the list
# Check if the length of the current string is greater than the length of the longest string so far
# If it is, update the longest string variable
# Print the longest string
str_list = ["Hello","I","am","Athish"]
longest_str = ""
for string in str_list:
    if len(string) > len(longest_str):
        longest_str = string 
print(longest_str)