# Without Def fuction
# Define the length of the sequence to generate
# Initialize the first two values in the sequence
# Generate the rest of the sequence using a for loop
# Calculate the next value in the sequence by adding the two previous values
# Append the next value to the sequence
# Print the final sequence

length = 10
fibonacci = [0,1]
for i in range(2,length):
    next_val = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_val)
    print(fibonacci)

# Or With Def Function
# Define a function to generate the Fibonacci sequence
# Initialize the first two values in the sequence
# Generate the rest of the sequence using a for loop
# Calculate the next value in the sequence by adding the two previous values
# Append the next value to the sequence
# Return the final sequence
# Define the length of the sequence to generate
# Call the function to generate the sequence
# Print the final sequence
def generate_fibonacci(length):
    fibonacci = [0,1]
    for i in range(2,length):
           next_val = fibonacci[i-1] + fibonacci[i-2]
           fibonacci.append(next_val)
           return fibonacci
length = 10
fibonacci = generate_fibonacci(length) 
print(fibonacci)