# Take an integer as input
# Loop through numbers 1 t 10
# Calculare the product of the input and the loop variable
# Print out the multiplication table
num = int(input("Enter a number:"))
for i in range(1,11):
    product = num * i
    print(num,"x",i,"=",product)