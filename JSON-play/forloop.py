# cities = ['boston.', "newton", "Chelmsford"]
# for city in cities:
#     print(city)
# print("inside the loop")
# print("Outside the loop")
import json
from ftplib import print_line
from pkgutil import get_data

# Create and populate a Python dictionary (equivalent to a JSON object)
data = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "skills": ["Python", "QA Management", "Software Testing"]
}

# Convert the Python dictionary to a JSON string (optional)
json_data = json.dumps(data, indent=2)
data_dict = json.loads(json_data)

# Print JSON string
print("JSON Object:")
print(json_data)
# print_line()
print("\n"+ data_dict["name"])
print("\n"+ str(data_dict["age"]))
print( "\n"+data_dict["skills"][1])
print("-------"*40)
print(json_data.find("age"))
print(json_data.find("name"))
print(data_dict)
print(data_dict.pop("skills")[0])
print(data_dict.get("skills"))
print(data_dict.get("name"))

# //print()
# print(json_data["skills"}[1])


