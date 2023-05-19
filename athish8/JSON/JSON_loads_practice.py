# JSON to Python
import json
data = '{"name" : "Athish", "age" : 12, "city" : "Bribane"}'
data = json.loads(data)
print(data)