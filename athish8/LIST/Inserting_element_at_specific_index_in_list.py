# Without Def
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element_to_insert = 99
index_to_insert_at = 3
my_list.insert(index_to_insert_at, element_to_insert)
print("List after insertion:", my_list)

# With Def
def insert_element_at_index(input_list, element, index):
    input_list.insert(index, element)
    return input_list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element_to_insert = 99
index_to_insert_at = 3
result = insert_element_at_index(my_list, element_to_insert, index_to_insert_at)
print("List after insertion:", result)
