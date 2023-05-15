# Create a list of data
data = ['Apple', 'Banana', 'Cherry', 'Durian']

# Using with statement
with open('output.txt', 'w') as file:
    # Write each item to the file
    for item in data:
        # Apply some condition to filter the items
        if len(item) > 5:
            # Write the filtered items
            file.write(item + '\n')
