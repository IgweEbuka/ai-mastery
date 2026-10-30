"""
- If statements can also be written on a single line. But it is case specific. And can't handle booleans except indented.
"""
age = 20
print("I am legal") if age > 18 else print("Underage")

# Exercise Level 1

#1
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive.")
else:
    if 18 - age == 1:
        print("You should be able to learn to drive in a year.")
    else:
        print(f"You need {18 - age} more years to learn how to drive.")


# #2
my_age = int(input("What is my age: "))
your_age = int(input("What is your age: "))

if my_age > your_age:
    if my_age - your_age == 1:
        print('I am one year older than you.')
    else:
        print(f"I am {my_age - your_age} years older than you.")
elif your_age > my_age:
    if your_age - my_age == 1:
        print('You are one year older than me.')
    else:
        print(f"You are {your_age - my_age} years older than me.")
else:
    print('We are the same age.')

# #3

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is less than {b}.")
else:
    print(f"{a} and {b} are equal.")


# Exercise Level 2

#1
score = int(input("Enter student grade: "))
grade = None
if score <= 59:
    grade = "F"
elif score <= 69:
    grade = "D"
elif score <= 79:
    grade = "C"
elif score <= 89:
    grade = "B"
else:
    grade = "A"

print(f"Student Grade = {grade}")

#2 

month = input("What month are we in? ")
month.capitalize
if month == 'September' or "October" or "November":
    print("The season is Autumn.")
elif month == "December" or "January" or "February":
    print("The season is Winter.")
elif month == 'March' or "April" or 'May':
    print("The season is Spring.")
else:
    print("The season is Summer.")

#3 

fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = input("Name a fruit: ")
new_fruit = new_fruit.lower()

if new_fruit in fruits:
    print(fruits)
else:
    fruits.append(new_fruit)
    print(fruits)


# Exercise Level 3

# 1

player ={
    'first_name': 'John',
    'last_name': 'Ikemu',
    'age': 20,
    'country': 'Nigeria',
    'is_married': True,
    'skills': ['Outside Curler', 'Phenominal Finishing', 'One-Time Pass', 'Acceleration Burst', 'Power Shot'],
    'address': {
        'street': 'Onne',
        'zipcode': '02210'
    }
    }

if 'skills' in player:
    skills = player['skills']
    print(skills[len(skills) // 2])

if 'skills' in player:
    print('Shadow Hunt' in player['skills'])

if player['is_married'] and player['country'] == 'Nigeria':
    print(f"{player['first_name']} {player['last_name']} lives in {player['country']}. He is married.")