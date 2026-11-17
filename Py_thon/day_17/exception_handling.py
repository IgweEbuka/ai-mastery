"""
- Python uses try and accept to handle error gracefully.
- Gracefully handling errors prevents the application from crashing.
- Going in this order:
    > try => Run a code.
    > except(may or may not have a condition) => execute this code when there is an exception.
    > else => No exceptions? Always runs with the try block.
    > finally => Always run this.
- To unpack arguements in python we use * for tuples and ** for dictionaries.
- We can also unpack in a range function expecting a start and an end.
- When using *rest to print gives out the all in a list together. But using rest without the * makes the remaining items into a list of their own.
    The above situations refer to tuples and lists.
- To do the same thing for dictionaries use ** before the dictionary name.
- In terms of packing. If unsure of the amount of list or tuple elements needed by a function use *args.
- Spreading in python can be done to both lists and tuples.
- If we are interested in an index of a list, we use enumerate built-in function to get the index of each item in the list.
- Sometimes we would like to combine lists when looping through them in this case we use ZIP.
"""

# Excption Handling

# try:
#     code in this block if things go well
# except:
#     code in this block run if things go wrong

"""
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
"""

# Unpacking & Packing

lst = [10, 11, 20, 21, 30]

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

first, second, third, *rest = lst

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'John', 'country':'USA', 'city':'Washington', 'age':21}
print(unpacking_person_info(**dct))

# Packing

def max_multi(*args):
    sotal = 1
    for i in args:
        sotal *= i
    return sotal

print(max_multi(1,2,3,4,5,6))

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

# Spreading in python

s_1 = (1, 2, 3, 4, 5)
s_2 = (6, 7, 8)
main = (0, *s_1, *s_2)
print(main)

# Enumerate

countries = ('Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland')
for index, i in enumerate(countries):
    if i == 'Denmark':
        print(f'The country {i} has been found at index {index}.')

# Zip

Ars = ['AK117', 'Bal27', 'Oden', 'Type 19', 'Grau']
SMGs = ['Chicom', 'Uss9', 'Static', 'Sten', 'Cordite']

ars_and_smgs = []

for ar, smg in zip(Ars, SMGs):
    ars_and_smgs.append({'ARs': ar, 'SMGs': smg})
print(ars_and_smgs)

# Exercises

# 1

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

*first_5 , es, ru = names
Nordic_countries = first_5
print(Nordic_countries, es, ru)