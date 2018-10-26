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

mydict={ 'ip_address' : '1.2.3.4',
         'gateway' : '1.2.3.1',
         'idiots' : [1,3,5]}

mylist=[ "fudge", "candy is delicious", 99, mydict, "boo"]

pprint(mylist)

print(json.dumps(mylist),indent=4)

print(yaml.dump(mylist,default_flow_style=False))

with open("jsonfile.json", "w") as f:
    json.dump(mylist,f,indent=4)

with open("yamlfile.yml", "w") as f:
    f.write(yaml.dump(mylist,default_flow_style=False))




