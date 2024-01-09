# Using Sorted Function
# Without Def
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list_desc = sorted(my_list, reverse=True)
print(sorted_list_desc)

# With Def
def sort_desc(lst):
    return sorted(lst, reverse=True)

my_list = [3, 1, 4, 1, 5, 7, 2, 4, 5, 3, 5]
sorted_list_desc = sort_desc(my_list)
print(sorted_list_desc)

# Using Sort Function
# Without Def
my_list = [3, 1, 4, 1, 5, 8, 2, 2, 5, 3, 5]
my_list.sort(reverse=True)
print(my_list)

# With Def
def sort_desc_inplace(lst):
    lst.sort(reverse=True)

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sort_desc_inplace(my_list)
print(my_list)