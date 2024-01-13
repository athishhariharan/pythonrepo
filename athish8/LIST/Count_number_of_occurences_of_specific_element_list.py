# Without Def
my_list = [1, 2, 3, 4, 2, 5, 2]
element_to_count = 2
count = my_list.count(element_to_count)
print(f"The element {element_to_count} appears {count} times in the list.")

# With Def
def count_element_occurrences(lst, element):
    return lst.count(element)
my_list = [1, 2, 3, 4, 2, 5, 2]
element_to_count = 2
occurrences = count_element_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} appears {occurrences} times in the list.")
