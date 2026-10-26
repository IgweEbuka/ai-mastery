'''
- Negative and Postive indexing applies to lists.
- Unpacking also applies to lists.
- Slicing is applicable here as well.
- In is used to check the presence of an item in a list.
- To add an item to the end of a list use .append().
- To insert at an index use .insert().
- To remove use .remove(), pop() removes a specified index and 'del' which removes an entire collection or a single item. 
- Use copy() to clone an original list so changes to the copy will not affect the main list.
- To join lists we can use (+) and extend() to add a list to the end of another list.
- index() returns the index of a specified item.
- count() is used to count how many time a specific item appears in a list.
- reverse() reverses the order of a list.
- Middle of a list where n is the length of the list: [(n - 1) // 2 : n // 2 + 1] 
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits

(fruits.insert(2, "grape"))
(fruits.index('mango'))
fruits.sort(reverse=True)


# Exercise Level 1

it_companies = ["Facebook", 'Google,', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[0] = "eBook"
it_companies.append('Zinox')
it_companies.insert(3, 'Playstation')
it_companies.sort()
n = len(it_companies)
mid = it_companies[(n - 1) // 2 : n // 2 + 1] 
del it_companies[0]
del it_companies[-1]
del it_companies[(n -1) // 2 : n // 2 + 1]
it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
both_ends = front_end + back_end
print(both_ends)

full_stack = both_ends.copy()
full_stack.index('Redux')
full_stack.insert(4, 'Python, SQL, and FastAPI')
print(full_stack)