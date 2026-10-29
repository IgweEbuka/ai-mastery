"""
- A collection of paired, unordered key:value data.
- Len() shows the number of key:valuse pairs in a dictionary.
- You access a dictionary by referring to its key name. 
- To avoid errors in cases of non-existent keys. First check if the key exists or use the .get() method. 
- To add a an item to a dictionary dict_name["Key"] = 'Value'
- To modify an existing key value => dict_name [existing value] = new_key
- To check if key is in a dictionary => Key in dict_name.
- Removal: pop(key);removes item with specific key, popitem(); removes last item and del removes a full item from a dictionary.
- .items() changes a dictionary to a list of tuples. 
- Keys as a list => dict_name.values() | values as a list => dict_name.keys()
- .copy() to copy a dictionary.
"""

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

person['height'] = '180cm'
del person['is_married']

# Exercise 1

dog = {}
dog["name"] = 'Jake'
dog["colour"] = 'Yellow'
dog["breed"] = 'Husky'
dog["legs"] = 4
dog["age"] = 20

student = {}

student["first_name"] = "John" 
student["last_name"] = "Walker"
student["gender"] = "Male"
student['age'] = 20
student['marital_status'] = 'married'
student['skills'] = ['React', 'Python', 'Java', 'HTML']
student['country'] = "Nigeria"
student['city'] = 'PH'
student['address'] = {'Street' : "Uche Street", "Zipcode" : "500101"}

student['skills'].append('CSS')
student.pop('age')
del student
print(student)

