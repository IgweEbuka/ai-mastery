"""
- Tuples are immutable.
- They don't need brackets to be created just the commas will do.
- Some methods: Count() to check how many times an item appears, len(), index()find an item by index and (+) to join.
- Positive & Negative indexing can work with tuples.
- Slicing works as well.
- del to delete a tuple.
"""

# Excercise Level 1

m_pty = ()
brothers = "David", "Mark", "Kene", "Pamo"
sisters = "Soso", "Flo", "Nengi", "Preye"

siblings = brothers + sisters

family_members = list(siblings)
family_members.sort()
family_members.insert(0, "Regina")
family_members.insert(0, "Chima")
print(family_members)

# Exercise Level 2

fruits = "Banana", "Apple"
veggies = "Tomato", "Spinach"
product = "Milk", "Honey"

food_stuff_tp = fruits + veggies + product

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt[2:4])
print(food_stuff_lt[0:3])
print(food_stuff_lt[3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries) 
