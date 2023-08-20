# Initialize an empty list to store reversed elements
# Iterate over each elemnt in the original list in reverse order
# Append the element to the reversed list

# With Def
def reverse_list(input_list):
    return input_list[::-1]

original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(reversed_list)

# Without Def
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print(reversed_list)