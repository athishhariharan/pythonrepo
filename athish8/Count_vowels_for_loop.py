# Define the input string
# Define a variable to store the vowel count
# Define a string containing all vowels, both upper and lowercase
# Loop over each character in the string
# If the character is not a vowel, skip to the next iteration
# Otherwize, increment the vowel count
# Print the final vowel count
input_string = "Athish"
vowel_count = 0
vowels = "aeiouAEIOU"
for char in input_string:
    if char not in vowels:
        continue
    vowel_count += 1 
print(f"The number of vowels in {input_string} is {vowel_count}")