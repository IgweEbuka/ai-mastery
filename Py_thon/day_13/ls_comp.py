"""
- The compact way of creating a list.
- Faster than using a loop.
- Syntax => [expression for i in iterable if condition].
- Lambda function is a small anonymous function without a name.
    It can take any number of arguments, but can only have one expression.
    It is needed when we want to write an anonymous function inside another function.
- To create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression.
- Syntax => lambda parameter_1, param2, param3 : expression using param 1 - 3.
- The value can then be assigned to something, and printed.
- A lambda function can also be used inside a function. The arguments needed will increase by how many lambdas there are.
"""

# Example 1
list_of_listings = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_listings for number in row]

# Example 2
add_two_numbs = lambda a, b : a + b

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]

# Example 3
def power(x):
    return lambda n : x ** n

two_power_of_five = power(2)(5)


# Exercise Level: 1

# 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
esc_nums = [i for i in numbers if i <= 0]

# 2
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
flat_list = [num for row in list_of_lists for num in row]

# 3
seq = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]

# 4 
countries_1 = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = [
    [name.upper(), name[:3].upper(), capital.upper()]
    for group in countries_1
    for name, capital in group
]

# 5
countries_2 = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = [
    {'country': name.upper(), 'city': capital.upper()}
    for group in countries_2
    for name, capital in group
]

# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
result = [first + " " + last for group in names for first, last in group]

