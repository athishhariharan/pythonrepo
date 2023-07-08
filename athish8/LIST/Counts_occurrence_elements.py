# Intialize a list of numbers
# Iterate over each element in the list
# Check if each element matches with the given element
# Set count variable to 0
# If there is a match with the element variable, set count by 1 higher than the previous number
# Repeat Lines 3 and 5 until the entire list is over
# After Line 6 is over, the count variable will count how much elements are there

# Without Def
my_list = [1, 2, 3, 4, 1, 2, 1, 3, 1]
element = 1

count = 0
for item in my_list:
    if item == element:
        count += 1

print(f"The element {element} occurs {count} times in the list.")

# With Def
def count_occurrences(my_list, element):
    count = 0
    for item in my_list:
        if item == element:
            count += 1
    return count

my_list = [1, 2, 3, 4, 1, 2, 1, 3]
element = 1

occurrences = count_occurrences(my_list, element)
print(f"The element {element} occurs {occurrences} times in the list.")
