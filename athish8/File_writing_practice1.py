# File writing - Normal
file = open("file1.txt","w")
file.write("Hello World \n")
file.close()

#  File Writing - With and As
with open("file2.txt","w") as file:
    file.write("Hello World \n")

# File Writing - Normal
file = open("file1.txt","a")
file.write("I am Athish \n ")
file.close

# File Writing - With and As
with open("file2.txt", "a") as file:
    file.write("I am Athish \n")