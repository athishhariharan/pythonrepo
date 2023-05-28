# import json

# with open("prabha\JSON\practice.json") as json_file:
#     data = json.load(json_file)
#     for item in data["items"]:
#         print("Item:", item["name"])
#         print("Price:", item["price"])


import json

# Open the JSON file
with open("prabha\JSON\practice.json") as json_file:
    # Load the JSON data
    data = json.load(json_file)

    # Initialize a variable to store the total price
    total_price = 0

    # Iterate over each item in the "items" array
    for item in data["items"]:
        # Retrieve the name and price of the item
        name = item["name"]
        price = item["price"]

        # Check if the item price is greater than 10
        if price > 10:
            # Add the price to the total
            total_price += price

            # Print the name and price of the item
            print("Item:", name)
            print("Price:", price)

    # Print the total price
    print("Total Price:", total_price)



