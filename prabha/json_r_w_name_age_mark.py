import json

# Create an empty dictionary
data = {
    "name": "",
    "age": 0,
    "marks": {
        "science": 0,
        "english": 0,
        "maths": 0
    }
}

# Prompt the user for input
data["name"] = input("Enter name: ")
data["age"] = int(input("Enter age: "))

data["marks"]["science"] = float(input("Enter Science marks: "))
data["marks"]["english"] = float(input("Enter English marks: "))
data["marks"]["maths"] = float(input("Enter Maths marks: "))

# Write the dictionary to a JSON file
with open('data.json', 'w') as file:
    json.dump(data, file)

# Read the JSON file and load the data into a dictionary
with open('data.json', 'r') as file:
    loaded_data = json.load(file)


# Print the loaded data
print("Loaded data:")
print(loaded_data)
