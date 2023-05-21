import json
# JSON string
json_string = '''
{
    "name" : "Athish",
    "age" : 12,
    "city" : "Brisbane"
}
'''
# JSON Parsing
data = json.loads(json_string)
# Accessing values in the parsed JSON objects
name = data["name"]
age = data["age"]
city = data["city"]

print(name)
print(age)
print(city)