# Create a list of data
data = ['Apple', 'Banana', 'Cherry', 'Durian', 'Orange', 'fig', 'dates']

# Using with statement
with open('output.txt', 'a') as file:
    # Append each item to the file
    for item in data:
        # Apply some condition to filter the items
        if len(item) > 5:
            # Append the filtered items
            file.write(item + '\n')