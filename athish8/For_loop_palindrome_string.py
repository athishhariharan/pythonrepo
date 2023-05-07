
def is_palindrome(word):
    for i in range(len(word)):
        if word[i] != word[len(word)- i - 1]:
            return False
    return True

word = "Racecar"
if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")

