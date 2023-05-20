import json
# JSON to Python
json_string = '''
{
    "name" :"Athish",
    "age" : 12,
    "city" :"Brisbane",
    "marks" : {
        "English" : 93,
        "Maths" : 100,
        "Science" : 97
        },
    "family" : ["Tanish", "Prabha", "Hari"]

} '''
data = json.loads(json_string)

# Accessing values

family = data["family"]
print(family)

marks = data["marks"]["Maths"]
print(marks)


