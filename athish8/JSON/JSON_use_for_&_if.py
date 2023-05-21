import json
# JSON string
json_string = '''
{
    "students" : [
        {
          "name" : "Athish",
          "age" : 12,
          "grade" : "A"
        },
        { 
          "name" : "Tanish",
          "age" : 10,
          "grade" : "B"
        },
        {
          "name" : "Prabha",
          "age" : 37,
          "grade" : "A"
        }
    ]
}
'''
# JSON parsing
data = json.loads(json_string)
# Accessing and processing JSON data
for student in data["students"]:
    name = student["name"]
    age = student["age"]
    grade = student["grade"]

    # Check if the student's grade is "A"
    if grade == "A":
        print(f"{name} is an outstanding student.")

    # Check if the student is above a certain age
    if age > 12:
        print(f"{name} is above 12 years old.")

    # Check if the student's name starts with a specific letter
    if name.startswith("T"):
        print(f"{name} has a name starting with 'T'.")