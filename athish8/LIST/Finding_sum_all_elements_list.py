# Without Def
my_list = [1, 2, 3, 4, 5]
list_sum = sum(my_list)
print(f"Sum of all elements in the list: {list_sum}")

# With Def
def find_list_sum(input_list):
    list_sum = sum(input_list)
    return list_sum
my_list = [1, 2, 3, 4, 5]
result = find_list_sum(my_list)
print(f"Sum of all elements in the list: {result}")
