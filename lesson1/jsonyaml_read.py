#!/usr/bin/env python

"""
From the worksheet:

7. Write a Python program that reads both the YAML file and the JSON file
created in exercise6 and pretty prints the data structure that is returned.
"""

import json
import yaml
from pprint import pprint

with open("jsonfile.json", "r") as f:
    jsonfile=json.load(f)

with open("yamlfile.yml", "r") as f:
    yamlfile=yaml.load(f)

print("JSON:")
pprint(jsonfile)

print("YAML:")
pprint(yamlfile)




