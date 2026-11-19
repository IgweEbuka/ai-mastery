"""
- We usually store our data in different file formats. In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel).
- File handling in progamming is used to update, create, read and delete files.
- In python to handle data we use the built-in open function.
    Syntax > open('filename', mode).
    The mode there is a place holder for any these.
        "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
        "a" - Append - Opens a file for appending, creates the file if it does not exist
        "w" - Write - Opens a file for writing, creates the file if it does not exist
        "x" - Create - Creates the specified file, returns an error if the file exists
        "t" - Text - Default value. Text mode
        "b" - Binary - Binary mode (e.g. images)
    .read() is to read the whole text as a string. We can limit is by passing an int number along side it i.e read(number).
    .readline() reads only the first line.
    .readlines() reads all texts line by line and returns a list of those lines.
    .read().splitlines() does the same thing as readlines().
- Using with before open closes a file automatically.
- File types:
    .txt > These are mainly used for storing text.
    .json > JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.
        json.loads(json.obj) to convert a JSon to a dictionary.
        json.dumps(person, indent=4) to convert dictionary to JSON.
        We use encoding and indentation. Indentation makes the json file easy to read.
    .csv > CSV stands for comma seperated values. Used to store tabular data such as database or spreadsheet.
        Accessed using open.
        Reader() is used to read CSV.
    .xls > TO read excel files.
    .xml > structured data format which looks like HTML.
        Methods include:
        .parse > return element tree instance.
        .getroot > return root element of this tree.

"""
import os
import json
# import xlrd
import csv


# Opening Files for Reading: 
# The default mode of open is reading, so there is no need to specify.
# An open file has to be closed with the close() method.

f = open('./Py_thon/day_19/example.txt')
txt = f.read()
# print(type(txt))
# print(txt)
f.close()

with open('./Py_thon/day_19/Polyphia.txt') as j:
    lines = j.read().splitlines()
    # print(type(lines))
    # print("Great Polyphia songs:",lines)


# Opening Files for Writing and Updating: 
# "a" - append - will append to the end of the file, if the file does not exist it creates a new file.
# "w" - write - will overwrite any existing content, if the file does not exist it creates.

with open('./Py_thon/day_19/Polyphia.txt', 'a') as p:
    p.write("The Audacity")

with open('./Py_thon/day_19/Lorevenor_chars.txt', 'w') as l:
    l.write('Night')

# Deleting Files:
# We use the os model to remove files.

os.remove('./Py_thon/day_19/Lorevenor_chars.txt')

if os.path.exists('./Py_thon/day_19/example_2.txt'):
    os.remove('./Py_thon/day_19/example_2.txt')
else:
    # print("This file does't exist.")
    pass

# File Types:

# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
# print(type(person_dct))
# print(person_dct)
# print(person_dct['name'])

person = {
    "Name" : "John",
    "Country" : "Nigeria",
    "City" : "PH",
    "Playstyle" : "Haram"
}

# Converting dictionary to JSON
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

person_json = json.dumps(person, indent=4)
# print(type(person_json))
# print(person_json)

# Saving a JSON file
with open("./Py_thon/day_19/json_example.json", 'w', encoding='utf-8') as m:
    # json.dump(person, m, ensure_ascii=False, indent=4)
    pass

# File with csv Extension:

data =["name","country","city","skills"]
with open("./Py_thon/day_19/csv_example.csv", 'w') as k:
    # k.write("data")
    pass

# # with open('./files/csv_example.csv') as f:
# #     csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             # print(f'Column names are :{", ".join(row)}')
#             line_count += 1
#         else:
#             # print(
#             #     f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
#             line_count += 1
#     # print(f'Number of lines:  {line_count}')

# File with xlsx Extension:
# We need to install the xlrd package.


"""
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
"""

# File with xml Extension:
# In xml tags are not predefined.

# with open("./Py_thon/day_19/xml_example.xml", 'w') as w:
#     # w.write('<?xml version="1.0"?>')

import xml.etree.ElementTree as ET
tree = ET.parse('./Py_thon/day_19/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)