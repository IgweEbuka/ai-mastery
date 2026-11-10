"""
- Functions are treated as high class citizens in python.
- A function can be returend as a result to another function.
- A function can also be taken as a parameter.
- Python allows a nested function to access the outer scope of the enclosing function.
- Python allows a function to be a return value.
- Decorators are python design patterns that allow a user to add new functionality to an existing object without changing its structure.
    To create an outer func we need an inner function with an inner wrapper function.
    Multiple decorators can be added to one function. excecuted from top to bottom.
    
"""

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

