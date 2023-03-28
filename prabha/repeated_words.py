import pdb
pdb.set_trace()
my_string = "the quick brown fox jumps over the lazy dog the quick brown fox"
words = my_string.split()
print(f"words: {words}")
word_set = set(words)
print(f"word_set: {word_set}")

for keyword in word_set:
    count = words.count(keyword)
    if count > 1:
        print(f"The word '{keyword}' appears {count} times in the string")
