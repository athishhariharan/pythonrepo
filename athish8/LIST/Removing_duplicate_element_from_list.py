# Without Def
my_list = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 8, 9]
unique_list = list(set(my_list))
print("Original List:", my_list)
print("List with Duplicates Removed:", unique_list)

# With Def
def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list
my_list = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 8, 9]
result = remove_duplicates(my_list)
print("Original List:", my_list)
print("List with Duplicates Removed:", result)
