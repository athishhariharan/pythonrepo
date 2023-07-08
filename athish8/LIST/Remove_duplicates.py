# Without def - numbers
# Initialize an empty list to store unique elements
# Iterate over each element in the original list
# Check if the element is not already in the unique list
# Add the unique element to the unique list


# Without def - string
my_list = ["apple", "banana", "orange", "apple"]
unique_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)


# With Def
# Initialize an empty list to store unique elements
# Iterate over each item in the input list
# Check if the element is not already in the unique list
# If it's not in the unique list, append it
# Return the list with duplicates removed

def remove_duplicates(lst):
    return list(set(lst))
my_list = [1, 2, 3, 2, 4, 1, 5, 3, 5]
unique_list = remove_duplicates(my_list)

print(unique_list)






