# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET

def getdata():
    tree = ET.parse('data.xml')
    root = tree.getroot()

    show(root)

def show(x):
    for e in x:
        print(e.attrib.get('name') if e.attrib else "" ,  e.text if e.text else "")
        show(e)


getdata()

