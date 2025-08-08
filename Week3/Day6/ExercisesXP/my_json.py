import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
# Step 1: Load the JSON string
#
#     Import the json module.
#     Use json.loads() to parse the JSON string into a Python dictionary.
#
#
# Step 2: Access the nested “salary” key
#
#     Access the “salary” key using nested dictionary access (e.g., data["company"]["employee"]["payable"]["salary"]).
#     Print the value of the “salary” key.
#
#
# Step 3: Add the “birth_date” key
#
#     Add a new key-value pair to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
#     Replace "YYYY-MM-DD" with an actual date.
#
#
# Step 4: Save the JSON to a file
#
#     Open a file in write mode ("w").
#     Use json.dump() to write the modified dictionary to the file in JSON format.
#     Use the indent parameter to make the JSON file more readable.

json_dict = json.loads(sampleJson)
print(json_dict["company"]["employee"]["payable"]["salary"])

json_dict["company"]["employee"]["birth_date"] = "1999-09-22"

file = open("dump.json", "w")
json.dump(json_dict, file, indent="\t")
file.close()
