# Without Def
my_list = [1, 2, 3, 4, 3, 5]

element_to_remove = 3

if element_to_remove in my_list:
    my_list.remove(element_to_remove)
    print(f"First occurrence of {element_to_remove} removed: {my_list}")
else:
    print(f"{element_to_remove} not found in the list")

# With Def
def remove_first_occurrence(my_list, element_to_remove):
    if element_to_remove in my_list:
        my_list.remove(element_to_remove)
        print(f"First occurrence of {element_to_remove} removed: {my_list}")
    else:
        print(f"{element_to_remove} not found in the list")

# Example usage
my_list = [1, 2, 3, 4, 3, 5]
element_to_remove = 3
remove_first_occurrence(my_list, element_to_remove)
    