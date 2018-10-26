#!/usr/bin/env python

"""
From the worksheet:

8. Write a Python program using ciscoconfparse that parses this config file.
Note, this config file is not fully valid (i.e. parts of the configuration are missing).
The script should find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO')
and for each crypto map entry print out its children.

9. Find all of the crypto map entries that are using PFS group2

10. Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name).
Print these entries and their corresponding transform set name.
"""

from ciscoconfparse import CiscoConfParse
from pprint import pprint
import re

source_cfg=CiscoConfParse("cisco_ipsec.txt")

print("Crypto Line Entries for Exercise #8:")
cryptos=source_cfg.find_objects(r"^crypto\ map\ CRYPTO")
for c in cryptos:
    print(c.text)
    for cline in c.children:
        print(cline.text)

print ("done with #8.\n\n")

print("Searching for PFS group2, exercise 9. These use Group 2:")
groupers=source_cfg.find_objects(r"group2")
for c in groupers:
    muck=(c.parent)
    print(muck.text)
    for cline in muck.children:
        print(cline.text)

print ("done with #9.\n\n")




print("Searching for entries not AES, exercise 10:")
noaes=source_cfg.find_objects_wo_child(r"^crypto\ map\ CRYPTO", childspec="transform-set AES")
for c in noaes:
    muck=(c.parent)
    print(muck.text)
    for cline in muck.children:
        if 'transform' in cline.text:
            match=re.search(r"transform-set (.*)$", cline.text)
            encryption=match.group(1)
            print("Uses: " + encryption)

print ("done with #10.\n\n")

