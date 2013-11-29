#!/usr/bin/python

import xml.etree.ElementTree as ET
import sys

def enumerate_classes(root):
    name_nodes = root.findall("compound[@kind='class']/name")
    class_names = []
    for node in name_nodes:
        class_names.append( node.text)
    return class_names

if len(sys.argv) < 2:
    print "Please provide the file you wish to parse"
    exit()
tree = ET.parse(str(sys.argv[1]))
root = tree.getroot()
print enumerate_classes(root)
