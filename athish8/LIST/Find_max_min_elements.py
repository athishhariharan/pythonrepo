# Without Def
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_element = my_list[0]
min_element = my_list[0]

for element in my_list:
    if element > max_element:
        max_element = element
    if element < min_element:
        min_element = element

print("Maximum element:", max_element)
print("Minimum element:", min_element)

#With Def
def find_max(lst):
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element

def find_min(lst):
    min_element = lst[0]
    for element in lst:
        if element < min_element:
            min_element = element
    return min_element

my_list = [3, 4, 4, 7, 5, 8, 2, 6, 5, 3, 5]

max_element = find_max(my_list)
min_element = find_min(my_list)

print("Maximum element:", max_element)
print("Minimum element:", min_element)
