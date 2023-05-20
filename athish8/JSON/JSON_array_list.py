import json
# JSON to Python
json_string = '''
{    
    "name" : "Athish",
    "age" : 12,
    "hobbies" : ["coding", "puzzles", "gaming"]

}
'''
data = json.loads(json_string)
# Accessing values in a JSON array
hobbies = data["hobbies"]
first_hobby = hobbies[0]
last_hobby = hobbies[-1]
print(hobbies)
print(first_hobby)
print(last_hobby)
# Modifying values in a JSON array
data["hobbies"].append("cycling")
data["hobbies"][1] = "playing"
# Python to JSON
json_string_modified = json.dumps(data)
print(json_string_modified)