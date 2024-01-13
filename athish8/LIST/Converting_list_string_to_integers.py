# Without Def
string_list = ['1', '2', '3', '4', '5']
int_list = [int(x) for x in string_list]
print(int_list)

# With Def
def convert_to_integers(string_list):
    return [int(x) for x in string_list]
string_list = ['1', '2', '3', '4', '5']
int_list = convert_to_integers(string_list)
print(int_list)
