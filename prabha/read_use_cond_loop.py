# Using with statement
with open('prabha\data.txt', 'r') as file:
    # Read each line from the file
    for line in file:
        # Apply some condition to filter the lines
        if line.startswith('A'):
            # Print the filtered lines
            print(line.strip())
