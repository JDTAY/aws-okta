import os
import json
import requests

# Change to the location of your terraform state file
rootdir = ""
print("finding all .tfstate files found at " + rootdir)

tfstate_list = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('.tfstate'):
            tfstate_list.append(os.path.join(subdir, file))

for state in tfstate_list:
    print("Iterating through the JSON object found at path " + state)
    with open (state) as file:
        json_object = json.load(file)
        # print(json_object)
        # do something

