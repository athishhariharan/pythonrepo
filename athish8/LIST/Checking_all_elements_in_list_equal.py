# Without Def
my_list = [3, 3, 3, 3, 3]
are_all_elements_equal = all(element == my_list[0] for element in my_list)
print(are_all_elements_equal)
# Using set() to check uniqueness
# Replace line 3 and 4 with this
are_all_elements_equal_set = len(set(my_list)) == 1
print(are_all_elements_equal_set)

# With Def
def are_all_elements_equal(lst):
    # Using the built-in all() function
    return all(element == lst[0] for element in lst)

def are_all_elements_equal_set(lst):
    # Using set() to check uniquenessss
    return len(set(lst)) == 1

my_list = [3, 3, 3, 3, 3]
print(are_all_elements_equal(my_list))
print(are_all_elements_equal_set(my_list))

