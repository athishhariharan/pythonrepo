# 1. Sorting a list of integers in ascending order:

nums = [5, 2, 9, 1, 5, 6]
nums.sort()
print(nums) # Output: [1, 2, 5, 5, 6, 9]


# 2. Removing duplicates from a list:

fruits = ["apple", "banana", "orange", "apple", "kiwi", "banana"]
unique_fruits = list(set(fruits))
print(unique_fruits) # Output: ['banana', 'kiwi', 'orange', 'apple']


# 3. Counting the occurrences of an element in a list:

letters = ["a", "b", "c", "d", "a", "c", "b", "a"]
count_a = letters.count("a")
print(count_a) # Output: 3


# 4. Reversing a list:

nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums) # Output: [5, 4, 3, 2, 1]

# 5. Finding the maximum and minimum elements in a list:

nums = [1, 7, 3, 9, 4, 6]
max_num = max(nums)
min_num = min(nums)
print("Maximum number:", max_num) # Output: Maximum number: 9
print("Minimum number:", min_num) # Output: Minimum number: 1


# 6. Concatenating two lists:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_list = list1 + list2
print(new_list) # Output: [1, 2, 3, 4, 5, 6]


# 7. Slicing a list to get a sub-list:

nums = [1, 2, 3, 4, 5, 6]
sub_nums = nums[2:5]
print(sub_nums) # Output: [3, 4, 5]


# 8. Reversing a list:

numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print(reversed_numbers) # Output: [5, 4, 3, 2, 1]


# 9. Sorting a list in descending order:

numbers = [5, 2, 4, 1, 3]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers) # Output: [5, 4, 3, 2, 1]


# 10. Finding the maximum and minimum values in a list:

numbers = [5, 2, 4, 1, 3]
max_value = max(numbers)
min_value = min(numbers)
print("Max value:", max_value) # Output: Max value: 5
print("Min value:", min_value) # Output: Min value: 1


# 11. Checking if all elements in a list are equal:

numbers = [5, 5, 5, 5, 5]
all_equal = all(num == numbers[0] for num in numbers)
print("All elements are equal:", all_equal) # Output: All elements are equal: True


# 12. Splitting a list into chunks of a specific size:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3
chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]
print(chunks) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]


# 13. Removing the first occurrence of a specific element from a list:

numbers = [1, 2, 3, 2, 4, 2, 5]
numbers.remove(2)
print(numbers) # Output: [1, 3, 2, 4, 2, 5]


# 14. Finding the common elements between two lists:

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common_elements = list(set(a) & set(b))
print(common_elements) # Output: [3, 4]

# 15. Combining two lists into a list of tuples:

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = list(zip(names, ages))
print(people) # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


# 16. Finding the sum of all elements in a list:

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total) # Output: 15


# 17. Replacing all occurrences of a specific element in a list with a new value:

numbers = [1, 2, 3, 2, 4, 2, 5]
new_value = 0
numbers = [new_value if num == 2 else num for num in numbers]
print(numbers) # Output: [1, 0, 3, 0, 4, 0, 5]


# 18. Removing the last element from a list:

numbers = [1, 2, 3, 4, 5]
numbers.pop()
print(numbers) # Output: [1, 2, 3, 4]

# 19. Counting the number of occurrences of a specific element in a list:

numbers = [1, 2, 3, 2, 4, 2, 5]
count = numbers.count(2)
print(count) # Output: 3


# 20. Converting a list of strings to integers:

string_numbers = ["1", "2", "3", "4", "5"]
integer_numbers = [int(num) for num in string_numbers]
print(integer_numbers) # Output: [1, 2, 3, 4, 5]


#21. Removing duplicate elements from a list:

numbers = [1, 2, 3, 2, 4, 2, 5]
unique_numbers = list(set(numbers))
print(unique_numbers) # Output: [1, 2, 3, 4, 5]

# 22. Checking if a list contains a specific element

numbers = [1, 2, 3, 4, 5]
has_three = 3 in numbers
print(has_three) # Output: True


# 23. Inserting an element at a specific index in a list:

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 0)
print(numbers) # Output: [1, 2, 0, 3, 4, 5]


#24. Combining multiple lists into a single list:

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
combined = a + b + c
print(combined) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 25. Sorting a list in ascending order:

numbers = [5, 2, 4, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers) # Output: [1, 2, 3, 4, 5]

# 26. Removing elements from a list that meet a certain condition:

numbers = [1, 2, 3, 4, 5]
filtered_numbers = [num for num in numbers if num % 2 == 0]
print(filtered_numbers) # Output: [2, 4]


# 27. Reversing the order of elements in a list:

numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))
print(reversed_numbers) # Output: [5, 4, 3, 2, 1]


# 28. Finding the index of the first occurrence of an element in a list:

numbers = [1, 2, 3, 4, 5]
index_of_three = numbers.index(3)
print(index_of_three) # Output: 2


# 29. Checking if all elements in a list meet a certain condition:

numbers = [2, 4, 6, 8, 10]
all_even = all(num % 2 == 0 for num in numbers)
print(all_even) # Output: True

# 30. Merging two lists of dictionaries based on a shared key:

a = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
b = [{"id": 1, "age": 25}, {"id": 2, "age": 30}]
merged = [{**x, **y} for x in a for y in b if x["id"] == y["id"]]
print(merged) # Output: [{'id': 1, 'name': 'Alice', 'age': 25}, {'id': 2, 'name': 'Bob', 'age': 30}]

# 31. Splitting a list into smaller sublists:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3
chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]
print(chunks) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

#32. append(): This function adds an element to the end of the list.

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
Output: [1, 2, 3, 4]

# 33. extend(): This function extends the list by appending elements from an iterable.

my_list = [1, 2, 3]
new_elements = [4, 5, 6]
my_list.extend(new_elements)
print(my_list)
Output: [1, 2, 3, 4, 5, 6]


# 34. insert(): This function inserts an element at a specific index in the list.

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)
Output: [1, 4, 2, 3]

# 35. remove(): This function removes the first occurrence of an element from the list.

my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)
Output: [1, 3, 2]


# 36. pop(): This function removes and returns the element at the specified index.

my_list = [1, 2, 3]
popped_element = my_list.pop(1)
print(my_list)
print(popped_element)
Output: [1, 3]
2

# 37. clear(): This function removes all elements from the list.

my_list = [1, 2, 3]
my_list.clear()
print(my_list)
Output: []


# 38. index(): This function returns the index of the first occurrence of an element in the list.

my_list = [1, 2, 3, 2]
index_of_two = my_list.index(2)
print(index_of_two)
Output: 1

# 39. count(): This function returns the number of times an element appears in the list.

my_list = [1, 2, 3, 2]
count_of_two = my_list.count(2)
print(count_of_two)
Output: 2


# 40. sort(): This function sorts the elements of the list in ascending order.

my_list = [3, 1, 2]
my_list.sort()
print(my_list)
Output: [1, 2, 3]


# 41. reverse(): This function reverses the order of the elements in the list.

my_list = [1, 2, 3]
my_list.reverse()
print(my_list)
Output: [3, 2, 1]


