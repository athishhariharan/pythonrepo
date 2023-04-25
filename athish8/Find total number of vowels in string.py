# Initialize a variable 'string' with some string value
# Initialize a variable 'vowels' to a list of vowels
# Initialize a variable count 0
# Loop through each character in the string
# If the character is a vowel, increment the 'count' variable
# Print 'count' variable

# Vowels Only
string = "Athish"
vowels = ['a','e','i','o','u']
count = 0
for char in string.lower():
    if char in vowels:
        count += 1
print(count)

# No vowels
string = "Athish"
vowels = ['a','e','i','o','u']
count = 0
for char in string.lower():
    if char not in vowels:
        count += 1
print(count)