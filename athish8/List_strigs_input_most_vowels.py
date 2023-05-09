# Define a list of strings
# Initialize variables to hold the string with the most vowels and the number of vowels
# Loop through each string in the list 
# Initialize a variable to hold the number of vowels in the current string
# Loop through each character in the current string
# Check if the current character is a vowel
# If it is, increment the vowel count
# Check if the current string has more vowels than the previous string with the most vowels
# If it does, update the string with the most vowels and the vowel count
# Print the string with the most vowels
str_list = ["hello", "athish", "amazing"]
most_vowels_str = ""
most_vowels_count = 0
for string in str_list:
    vowels_count = 0
    for char in string:
        if char in "aeiouAEIOU":
            vowels_count += 1
    if vowels_count > most_vowels_count:
        most_vowels_str = string
        most_vowels_count = vowels_count

print(most_vowels_str)

