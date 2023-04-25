# Create a list of numbers
# Initialize an empty list called reversed_list
# Use a for loop to iterate over the original list in reverse order
# For each number in the original list, append it to the reversed_list
# After the loop has finished, print the reversed list

numbers = [1,2,3,4,5]
reversed_list = []
for i in range(len(numbers)-1,-1,-1):
   reversed_list.append(numbers[i])
print(reversed_list)