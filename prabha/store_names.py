# Define a list of names
names = ['John', 'Emily', 'Michael', 'Sophia', 'William', 'Olivia']

# Open a new file called 'names.txt' for writing
with open('names.txt', 'w') as file:
    # Write each name to the file on a separate line
    for name in names:
        file.write(name + '\n')
