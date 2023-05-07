# Define the input string to be checked for palindrome
# Initialize a boolean variable "is_palindrome" to True, assuming that the string is a palindrome
# Loop through the input string using a for loop and check if the character at the current indes "i" is equal to the character at the corresponding index counting from the end of the strinf
# If the characters are not equal, set the "is_palindrome" variable to False and break out of the loop since the string is not a palindrome
# After the loop, check if the "is_palindrome" variable is still True, and if so, print a message saying that the input string is a palindrome, otherwise, print a message saying that it is not a palindrome
input_str = "racecar"
is_palindrome = True
for i in range(len(input_str)):
    if input_str[i] != input_str[-1-i]:
        is_palindrome = False
        break
    if is_palindrome:
        print(f"{input_str} is a palindrome!")
    else:
        print(f"{input_str} is not a palindrome!")