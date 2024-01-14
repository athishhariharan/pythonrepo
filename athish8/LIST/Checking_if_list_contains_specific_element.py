# Without Def
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element_to_check = 5
if element_to_check in my_list:
    print(f"The element {element_to_check} is present in the list.")
else:
    print(f"The element {element_to_check} is not present in the list.")

# With Def
def contains_element(input_list, element):
    return element in input_list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element_to_check = 5
result = contains_element(my_list, element_to_check)
if result:
    print(f"The element {element_to_check} is present in the list.")
else:
    print(f"The element {element_to_check} is not present in the list.")
