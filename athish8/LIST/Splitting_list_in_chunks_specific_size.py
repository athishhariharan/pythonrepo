# Without Def 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3
chunks = [my_list[i:i + chunk_size] for i in range(0, len(my_list), chunk_size)]
print(chunks)

# With Def
def chunk_list(input_list, chunk_size):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3

result = chunk_list(my_list, chunk_size)
print(result)
