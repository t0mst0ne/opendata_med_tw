#!/usr/bin/env python
#coding:UTF-8

import xml.etree.cElementTree as ET
import pandas as pd 

tree = ET.ElementTree(file='36_1.xml')
root = tree.getroot()
root.tag
pd.set_option('display.max_columns', None)

mylist = [{child2.tag:child2.text for child2 in child_of_root } for child_of_root in root]
df = pd.DataFrame(mylist)
