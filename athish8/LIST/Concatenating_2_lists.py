# Without Def
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("Concatenated List:", concatenated_list)

# With Def
def concatenate_lists(lst1, lst2):
    return lst1 + lst2
list1 = [7, 8, 9]
list2 = [10, 11, 12]
concatenated_list = concatenate_lists(list1, list2)
print("Concatenated List:", concatenated_list)
