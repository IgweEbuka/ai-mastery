"""
- A set in an unordered, unindexed collection of unique items
- We use loops to access the items in a set.
- Can check for items using in.
- Can add and item to a set using add().
- Can add multiple items using update([])
- Can remove a specified item from a set usinig remove().
- pop() removes a randomized item from a set. Store it as something to retrieve it.
- Clear() to empty a set and del to destroy a set.
- Converting list to a set removes duplicates.
- Can join two sets using the union() or update() method or | symbol.
- Intersection returns a set of items which are in both the sets or using & symbol.
- <= checks if a set is a subset of another.
- Checking subset and superset:
    subset == issubset() & superset == superset()
- Difference returns a collection of items that seperates two sets. We can use .difference() or the - symbol.
- Symmetric difference (^) returns a set that contains all items from both sets, except items that are present in both sets.
- .isdisjoint() is used to check if two sets are joint or disjoint
"""

# Exercise Level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add('Twitter')
it_companies.update(['Youtube', 'Playstation', 'Xbox'])
it_companies.remove('IBM')
it_companies.pop()
print(it_companies)

# Exercise Level 2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A | B)
del A
del B

# Exercise Level 3

age = [22, 19, 24, 25, 26, 24, 25, 24]
new_age = set(age)
print(len(age), len(new_age))