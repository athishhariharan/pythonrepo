# Without Def
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = list(zip(list1, list2))
print(f"Combined list of tuples: {combined_list}")

# With Def
def combine_lists_to_tuples(list1, list2):
    combined_list = list(zip(list1, list2))
    return combined_list
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = combine_lists_to_tuples(list1, list2)

print(f"Combined list of tuples: {result}")
