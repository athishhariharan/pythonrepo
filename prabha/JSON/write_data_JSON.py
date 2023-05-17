# import json

# # JSON data to write
# data = {
#     "items": [
#         {
#             "name": "Item 1",
#             "price": 10.99
#         },
#         {
#             "name": "Item 2",
#             "price": 5.99
#         },
#         {
#             "name": "Item 3",
#             "price": 7.99
#         }
#     ]
# }

# # Open a file for writing
# with open("C:\\athishwork\\code\\pythonrepo\\output.json", "w") as json_file:

#     # Write the JSON data to the file
#     json.dump(data, json_file, indent=4)

# # Print a success message
# print("JSON data written to output.json file.")


# import json

# # JSON data to append
# new_data = {
#     "name": "Item 4",
#     "price": 12.99
# }

# # Load existing JSON data
# with open("output.json") as json_file:
#     existing_data = json.load(json_file)

# # Append new data to the existing data
# existing_data["items"].append(new_data)

# # Write the updated JSON data back to the file
# with open("output.json", "w") as json_file:
#     json.dump(existing_data, json_file, indent=4)

# # Print a success message
# print("JSON data appended to data.json file.")

import json

# JSON data to write
data = {
    "items": [
        {
            "name": "Item 1",
            "price": 10.99
        },
        {
            "name": "Item 2",
            "price": 5.99
        },
        {
            "name": "Item 3",
            "price": 7.99
        }
    ]
}

# Filter the items based on a condition
filtered_items = []
for item in data["items"]:
    # Check if the price is greater than 7
    if item["price"] > 7:
        filtered_items.append(item)

# Create a new data object with filtered items
filtered_data = {"items": filtered_items}

# Open a file for writing
with open("write_data", "w") as json_file:
    # Write the filtered JSON data to the file
    json.dump(filtered_data, json_file, indent=4)

# Print a success message
print("Filtered JSON data written to output.json file.")


