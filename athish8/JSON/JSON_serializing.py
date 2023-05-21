import json

# Python object
data = {
    "name": "Athish",
    "age": 12,
    "city": "Brisbane"
}

# Serializing (Python to JSON)
json_string = json.dumps(data)

print(json_string)

