# Without Def
my_list = [1, 2, 3, 4, 5]
my_list.pop()
print(my_list)

# With Def
def remove_last_element(lst):
    lst.pop()
my_list = [1, 2, 3, 4, 5]
remove_last_element(my_list)
print(my_list)
