# Without Def
my_list = [1, 2, 3, 4, 2, 5, 2]
old_element = 2
new_element = 99
for i in range(len(my_list)):
    if my_list[i] == old_element:
        my_list[i] = new_element
print(my_list)

# With Def
def replace_element(lst, old_elem, new_elem):
    for i in range(len(lst)):
        if lst[i] == old_elem:
            lst[i] = new_elem
my_list = [1, 2, 3, 4, 2, 5, 2]
replace_element(my_list, 2, 99)
print(my_list)
