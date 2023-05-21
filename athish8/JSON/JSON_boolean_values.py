import json
# JSON to Python
json_string = '''
{
    "name" : "Athish",
    "age" : 12,
    "is_student" : false
}
'''
data = json.loads(json_string)
# Accessing a boolean value in JSON
is_student = data["is_student"]
print(is_student)
# Modifiying a boolean value in Python
data["is_student"] = True
# Python to JSON
json_string_modified = json.dumps(data)
print(json_string_modified)