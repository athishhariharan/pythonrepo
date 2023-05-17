import json
data = {
    "name" : "Athish",
    "age" : 12,
    "postcode" : 4306
}
with open("example.json","w") as file:
    json.dump(data,file)