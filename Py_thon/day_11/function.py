"""
- A function is a reusable block of code designed to perform a certain task.
- If a fucntion has no return statment it returns none.
- A function can be passed with multiple arguements.
- Return stops further execution of a code similar to break.
- If a function has a defualt value, when that function is called the default value takes that space if there is no present value.
- We can create a function which can take arbitrary number of arguments by adding (*) before the parameter name.
- Default arguments come before arbitrary ones.
- Dictionary Unpacking: The (**) before a dictionary in a function call takes each key-value pair and turn it into a keyword argument.
    For this to work the key must match the parameters and must be a string.
- In call (**) unpacks dict into KW and in definition packs KW into a dict.
"""

# Excercise Level: 1

# 1
def add_two_numbers(x, y):
    summation = x + y
    return print(summation)

# 2
def area_of_circle(r):
    pi = 3.14
    area = round(pi * r * r, 2)
    return print(area)

# 3
def add_all_nums(*nums):
    total = 0
    for n in nums:
        if isinstance(n, bool) or not isinstance(n, (float,int)):
            print("Use numbers only!")
        total += n
    return total

# 4
def convert_celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

# 5
def check_grade(score):
    if score <= 44:
        return 'F'
    elif score <= 55:
        return 'D'
    elif score <= 60:
        return 'C'
    elif score <= 69:
        return 'B'
    elif score >= 70:
        return 'A'

# 6
def print_list(data):
    for n in data:
        print(n)

# 7
def reverse_list(arr):
    result = []
    for item in arr:
        result.insert(0, item)
    return result

# 8
def capitalize_list_items(items):
    return [item.capitalize() for item in items]

# 9
def add_item(arr, prop):
    result = []
    for item in arr:
        result.append(item)
    result.append(prop)
    return result

# 10
def remove_item(items, item):
    result = items.copy()
    if item in result:
        result.remove(item)
    return result
