import json

new_name = "whatever I want 3"

with open("exercise.json", "r+") as json_file:
    data = json.load(json_file)
    data["names"].append(new_name)
    json_file.seek(0)
    json.dump(data, json_file, indent = 4)
