# Define a list of numbers
# Sort the list in ascending order
# Get the length of the list
# Check if the length of the list is odd or even
# If it's even, get the middle two numbers and calcuate their average
# If it's odd, get the middle number
# Print the median
num_list = [1,2,3,4,5,6,7,8,9]
num_list.sort()
list_len = len(num_list)
if list_len % 2 == 0:
    mid_right = list_len// 2
    mid_left = mid_right - 1
    median = (num_list[mid_left] + num_list[mid_right]) / 2
else:
    mid = list_len // 2
    median = num_list[mid]
print("The median is:", median)