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
- Search is much better than match because it can look for the pattern throughout the text.
- Findall() returns all matches as a list.
- When using any of these without re.I. There is need for case sensitivity. So in a case of Python and python. Use Python|python or [Pp]ython to refer to this special case.
- To declare RegEx variable r''.
- Metacharacters of RegEx:
    # Square Bracket[] > To include upper and lower case of a character.
    # Escape character(\)> \d brings out individual digits. \d+ bring out digits one or more times.
    # Period(.) > As in [a]. making it so a and any character except newline. [a].+ takes a and whatever comes after it except for a new line.
    # Zero or more times(*) > [x].* any character zero or more times.
    # Zero or one more time(?) > r"[Ee]-?mail" the use of the ? implies that the - is optional.
- Quantifier in RegEx{} > r'\d{1,4}'
- Cart(^):
    # Starts with(^""): Whatever comes after this string.
    # Negotiation([^]): The exception on whatever comes after the ^. 
"""

import re
from collections import Counter

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


# Searching for All Matches Using findall
txt_3 = """There is a greenhill far away,
without a city wall
Python,
python"""

matches = re.findall('Python', txt_3, )
# print(matches)


# Replacing a Substring
txt_4 = """I love Rejoice. I love rejoice with all my heart."""

match_subbed = re.sub("[Rr]ejoice", 'Dragon Ball',  txt_4)
# print(match_subbed)

txt_glitch = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

unglitched = re.sub("%", "", txt_glitch)
# print(unglitched)


# Splitting Text Using RegEx Split
txt_5 = """I too like plantain. At this rate you could say that i am addicted to plantain. I can kill for plantain."""
vox = re.split("plantain", txt_5)
# print(vox)


# Writing RegEx Patterns
reg_pattern = r'rice'

txt_6 = "The top 3's of Rice have be the in this order. Number 1 Jollof rice. Number 2 white rice. Number 3 Fried rice."
soln = re.findall("rice", txt_6, re.I)
# print(soln)


# Exercises 

# 1

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
paragraph = paragraph.lower()
words = re.findall(r"\b\w+\b", paragraph)
word_counts = Counter(words)
most_frequent_word, count = word_counts.most_common(1)[0]
print(f"The most frequent word is '{most_frequent_word}' (appeared {count} times).")