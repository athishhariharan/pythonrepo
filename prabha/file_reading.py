# file = open("C:/athishwork/code/pythonrepo/prabha/functions.py","r")
# content = file.read()
# file.close()
# print(content)

# file = open("C:/athishwork/code/pythonrepo/prabha/functions.py", "w")
# content = "This is the content that will be written to the file."
# file.write(content)
# file.close()


# with open("C:/athishwork/code/pythonrepo/prabha/functions.py", "a") as file:
#     file.write(" my name is prabha\n")


# Open file in 'write' mode and write a line to it
with open("C:/athishwork/code/pythonrepo/prabha/example6.txt", "w") as file:
    file.write('Hello, world!\n')


    file = open("C:/athishwork/code/pythonrepo/prabha/example6.txt", "w")
file.write('Hello, world!\n')
file.close()


# Open file in 'append' mode and append another line to it
with open("C:/athishwork/code/pythonrepo/prabha/example6.txt", "a") as file:
    file.write('This is a new line!\n')

# Open file in 'append' mode and append another line to it
file = open("C:/athishwork/code/pythonrepo/prabha/example6.txt", "a")
file.write('This is a new line!\n')
file.close()
