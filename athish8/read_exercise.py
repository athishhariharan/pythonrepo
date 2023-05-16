
# File Reading - Normal
file = open("athish8\example1.txt","r")
content = file.read()
file.close()
print(content)

# File Reading - With and As
# Open the file for reading
# Read the contents of the file
# Display the contents of the file
with open('athish8\example1.txt') as file:
    content = file.read()
print(content)

# File Reading - Normal
file = open("athish8/example1.txt","r")
content = file.readline()
file.close()
print(content)

# # File Reading - With and As
with open("athish8\example1.txt","r") as file:
    content = file.readlines()[4]
print(content)

