# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET

def getdata():
    tree = ET.parse('data.xml')
    root = tree.getroot()

    find(root)
    show(root)

def find(root):
    for country in root.findall('country'):
        rank = country.find('rank').text
        name = country.get('name')
        print(name, rank)

    print('--------------------',end='\n\n')

def show(x):
    for e in x:
        print(e.tag,e.attrib.get('name') if e.attrib else "" ,  e.text if e.text else "")
        show(e)


getdata()

