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

# Exercise Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
n = len(ages)
ages.sort()
ages.insert(0, ages[0])
ages.append(ages[-1])
print(ages)
mid = ages[(n - 1) // 2 : n // 2 + 1]
median_age = sum(mid) / len(mid)
print(median_age)
average_age = sum(ages) / n
print(average_age)
print(max(ages) - min(ages))

# Exercise Level 3

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

mid = (len(countries) + 1) // 2        # (195 + 1) // 2 = 98
first_half = countries[:mid]
second_half = countries[mid:]
(first_half)
(second_half)

mal = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = mal
print(first, second, third)
print(scandic_countries)