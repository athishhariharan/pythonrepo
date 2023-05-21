import json

# JSON string
json_string = '''
{
    "name" : "Athish",
    "age" : 12,
    "city" : "Brisbane",
    "hobbies" : ["coding", "puzzles", "gaming"]
}
'''

# JSON parsing with error handling
try:
    data = json.loads(json_string)
    print("JSON parsing successful")
    # Accessing a non-existent key
    if "address" in data:
        print(data["address"])
    else:
        print("Key 'address' does not exist")
except KeyError as e:
    print("KeyError:", str(e))
except json.JSONDecodeError as e:
    print("JSONDecodeError:", str(e))
