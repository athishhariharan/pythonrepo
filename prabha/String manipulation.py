import pdb
#pdb.set_trace()
# find lenth of string 
string = input("Enter a string: ")
length = len(string)
#print("The length of the string is", length)

string1 = string.split()
#print(string1)
count = len(string1)

for i in range(1, count):
    for str in string1:
        if str == string1[i]:
            print(f"Than matched string is {str}")
        # else:
        #     print("string is not macthed")
    




