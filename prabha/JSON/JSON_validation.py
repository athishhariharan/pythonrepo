import json

# JSON string
json_string = '''
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
'''

# JSON validation
try:
    json_object = json.loads(json_string)
    print("Valid JSON")
except json.JSONDecodeError as e:
    print("Invalid JSON:", str(e))
