"""
- Functions are treated as high class citizens in python.
- A function can be returend as a result to another function.
- A function can also be taken as a parameter.
- Python allows a nested function to access the outer scope of the enclosing function.
- Python allows a function to be a return value.
- Decorators are python design patterns that allow a user to add new functionality to an existing object without changing its structure.
    To create an outer func we need an inner function with an inner wrapper function.
    Multiple decorators can be added to one function. excecuted from top to bottom.
    Parameters can also be accepted in a wrapper function.
- There are various built in functions;
    > The map function, takes a fucntion and an iterable as arguements and gives out an iterable with the function applied to each iterable.
    > The filter function, It filters the items that satisfy the filtering criteria using a predetermined function.
    > The reduce function, it takes a function that accpets 2 elements, then applies that function to the first 2 items in an iterable then moves that process downwards returning 1 value.
"""

from functools import reduce

# A closure
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

# A return value
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
# print(result(3))       # 9

# Decorators
def lowercase_decorator(function):
    def wrapper():
        func = function()
        make_lowercase = func.lower()
        return make_lowercase
    return wrapper

@lowercase_decorator
def greeting():
    return "WELCOME OF PYTHONN"

# Built in higher-order-functions

# 1 Map
namesss = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6]
def change_to_upper(name):
    return name.upper()

def plus_up(n):
    return n * 2

names_raised = list(map(lambda name: name.upper(),namesss))
# print((names_raised))

num_math = map(lambda num: num * 2, numbers)
# print(list(num_math))

# 2 Filter
numbersss = [1, 2, 3, 4, 5] 

def is_even(n):
    if n % 2 == 0:
        return True
    return False

def is_odd(n):
    if n % 2 == 1:
        return True
    return False

even_numbers = list(filter(is_even, numbersss))
odd_numbers = tuple(filter(is_odd, numbersss))
# print(even_numbers)
# print(odd_numbers)

# 3 Reduce

def multiply_two(a, b):
    return a * b

numbers_all_multiplied = reduce(multiply_two, numbers)
# print(numbers_all_multiplied)

# Exercises

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1

upper_countries = list(map(lambda country: country.upper(), countries))
# print(upper_countries)

squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)

upper_names = list(map(lambda name: name.upper(), names))
# print(upper_names)

def land_countries(n):
    if 'land' in n:
        return True
    return False

filtered_countries = list(filter(land_countries, countries))
# print(filtered_countries)

def six_and_more(n):
    if len(n) >= 6:
        return True
    return False

six_length_only = list(filter(six_and_more, countries))
# print(six_length_only)

def starts_with_E(n):
    if n[0] == 'E':
        return True
    return False

starting_with_E = list(filter(starts_with_E, countries))
# print(starting_with_E)

squared = map(lambda x: x ** 2, numbers)
evens = filter(lambda x: x % 2 == 0, squared)
total = reduce(lambda a, b: a + b, evens) 


def count_starting_letters(countries):
    counts = {}
    for country in countries:
        letter = country[0]
        counts[letter] = counts.get(letter, 0) + 1
    return counts