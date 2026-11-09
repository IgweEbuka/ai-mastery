"""
- Modules are files containing a set of codes or functions which can be included to an application.
- They can be imported using (import).
- When importing you can name the import as something else by using as.
- They can also have their functions imported using: From Mod import func.
- There are specific in-built models that possess specific functions:
    * OS Module(import os): creating, remove a directory, changing current working directory, fetching its contents, changing and identifying the current directory.
    * SYS MOdule(import sys): The sys module provides functions and variables used to manipulate different parts of the Python runtime environment.
    * Statistiscs Module: This module provides functions for mathematical statistics of numerical data.
    * math: Module containing many mathematical operations and constants.
    * String Module: A module used to manipulate strings.
    * random module: A random module which gives us a random number between 0 and 0.9999.
        The random module:
        .choice(lst) = one random item.
        .sample(lst, k) = returns k items from cellection with no repetition.
        .choices(lst, k) = random choices from iterable using k.
        .random() = returns a float from 0.0 up to, but not including, 1.0.
        .randint(a, b) returns a random integer from a to b, with both ends included. 
        .randrange(start, stop, step) works like range(), so the stop value is excluded.
        .uniform(a, b) returns a random float between a and b.
        .shuffle(lst) = rearranges the list in place and returns None.
"""

def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

import random
import string


# Exercise Level: 1

# 1
def random_user_id():
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=6))

# 2
def user_id_gen_by_user():
    length = int(input("Number of characters: "))
    count = int(input("Number of IDs: "))
    chars = string.ascii_letters + string.digits

    for _ in range(count):
        print("".join(random.choices(chars, k=length)))


# Exercise Level: 2

# 1
def list_of_hexa_colours(n):
    hexa_chars = '0123456789abcdef'
    colours = []
    for _ in range(n):
        colour = "#" + "".join(random.choices(hexa_chars, k = 6))
        colours.append(colour)
    return colours

# 2
def list_of_rgb_colors(n):
    colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f'rgb({r}, {g}, {b})')
    return colors

# 3

def generate_colours(colour_type, n):
    if colour_type == "hexa":
        return list_of_hexa_colours(n)
    elif colour_type == "rgb":
        return list_of_rgb_colors
    else:
        raise ValueError(f"colour_type must be 'hexa' or 'rgb', got{colour_type!r}")

# Exercise Level: 3

# 1
def shuffle_list(lst):
    result = lst.copy()
    random.shuffle(result)
    return result
    
ages = [12, 49, 32, 23, 25, 10, 7]

# 2
def unique_random_number(count=7, low = 0, high = 9):
    return random.sample(range(low, high + 1), count)