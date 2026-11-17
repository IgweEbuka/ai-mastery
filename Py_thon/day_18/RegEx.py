"""
- A RegEx is a special text string used to find patterns in data.
- A RegEx can be used to check if some pattern exists in a different data type.
- To use RegEx we import the re module.
- Methods in thr re module:
    re.match() > searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
    re.search > Returns a match object if there is one anywhere in the string, including multiline strings.
    re.findall > Returns a list containing all matches.
    re.split > Takes a string, splits it at the match points, returns a list.
    re.sub: Replaces one or many matches within a string.
- 
"""

import re

# Match
txt = 'I love to watch Anime and Movies.'

match = re.match('I love to watch', txt, re.I)
# print(match)
span = match.span()
# print(span)
start, end = span
# print(start, end) 
substring = txt[start:end]
# print(substring) 


# Search
txt_2 = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match_2 = re.search('first', txt_2, re.I)
# print(match_2)
span_2 = match_2.span()
# print(span_2)
start_2, end_2 = span_2
# print(start_2, end_2)
substring_2 = txt_2[start_2:end_2]
# print(substring_2)