# Without Def
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list = my_list[2:6]  
print("Sub-list:", sub_list)

# With Def
def get_sub_list(lst, start, end):
    return lst[start:end]
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list = get_sub_list(my_list, 3, 7)  
print("Sub-list:", sub_list)
