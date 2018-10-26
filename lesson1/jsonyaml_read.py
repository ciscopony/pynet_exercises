#!/usr/bin/env python

"""
From the worksheet:

6. Write a Python program that creates a list. One of the elements of the list
should be a dictionary with at least two keys. Write this list out to a file using both
YAML and JSON formats. The YAML file should be in the expanded form.
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




