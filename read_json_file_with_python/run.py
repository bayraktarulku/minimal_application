import json

# Opening JSON file
f = open("data.json")

# returns JSON object as
# a dictionary
data = json.load(f)

# list
for c in data["certifications"]:
    print(c["name"], c["courses"])

# Closing file
f.close()
