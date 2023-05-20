import json
# JSON to Python
json_string = '''
{
     "name" : "Athish",
     "age" : 12,
     "address" : {
          "street" : "1 Main Street",
          "city" : "Brisbane",
          "state" : "QLD"
     }
}
'''
data = json.loads(json_string)
# Accessing nested values in a JSON object
street = data["address"]["city"]
street1 = data["address"]["state"]

print(street)
print(street1)
# Modifying nested value in a Python object
data["address"]["street"] = "473 Parkview Pde"

# Python to JSON
json_string_modified = json.dumps(data)
print(json_string_modified)