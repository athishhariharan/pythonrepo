# Take an integer as input
# Loop through rows
# Print stars in each row
n = int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")