"""
- While loops are used to execute a block repeatedly until the given condition is satisfied.
- If we are interested in running a block once the statement is satisfied we can use else.
- We can use break to get out of or stop the loop.
- Continue, skips the rest of a current pass in a loop.
- Using a for loop in different cases:
    String:
        i. for letter in language:, print(letter).
        ii. for i in range(len(language)):, print(i).
    Tuple:
        i. for num in numbers:, print(num).
    Dictionary:
        i. for key, valye in person.item():, print(key) -- This prints the keys and/or values.
    set:
        i. for x in set:, print(x).
- When break is used in a for loop it ends the loop.
- When continue is used it skips whatever is below it and restarts the loop.
- Range is used to return a list of parameters(start, stop, step).
- Else is used after a for loop when you intend to execute a message.
- Pass is used to avoid executing a loop or used as a placeholder to be replaced later.
- Reversed returns the reversed iteration of a given sequence.
"""

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    count = count + 1

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            pass

# Exercise Level 1

# 1
for i in range(0, 11):
    pass

count = 0
while count < 11:
    pass
    count += 1

# 2 
for i in range(10, -1, -1):
    pass

num = 10
while num != -1:
    pass
    num -= 1

# 3

for i in range(1, 8):
    pass

# 4

for row in range(8):
    # print(' '.join('#' * 8))
    pass

# for row in range(8):
#     for col in range(8):
#         print('#', end=' ')
#     print()

# 5

for x in range(11):
    # print(f"{x} X {x} = {x * x}")
    pass

# 6

skills = ['Python', 'Numpy','Pandas','Django', 'Flask'] 

for skill in skills:
    pass

for num in range(101):
    if num % 2 == 0:
        pass


# Exercise Level: 2

# 1
total = 0
for i in range(101):
    total += i
pass

# 2
jam = 0
for j in range(101):
    if j % 2 == 1:
        jam += j
pass

# Exercise Level: 3

# 1

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

for country in countries:
    if 'land' in country:
        pass

# 2

fruits = ['banana', 'orange', 'mango', 'lemon'] 

for fruit in reversed(fruits):
    pass