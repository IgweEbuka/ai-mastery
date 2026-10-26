# Creating a BST #

class LevelNode:
    def __init__(self, price):
        self.price = price
        self.left = None
        self.right = None

def insert(node, price):
    if node is None:
        return LevelNode(node)
    if price < node.price:
        node.left = insert(node.left, price)
    else:
        node.right = insert(node.right, price)
    return node

def search(node, target):
    if node is None or node.price == target:
        return node
    if target < node.price:
        return search(node.left, target)
    else:
        return search(node.right, target)


# Strings #

first_name = 'Ebuka'
last_name = 'Igwe'
game = 'WUWA'

full_string = 'I am %s %s. I love playing %s.' %(last_name, first_name, game)

# Strings and numbers

length = 10
breath = 5
perimeter = 2 * (length * breath)
sting = 'The perimeter of the square with length %dcm and breath %dcm is %.1fcm^2.' %(length, breath, perimeter)

genshin_DPS_Characters = ['Mavuika', 'Neuvi', 'Zibai', 'Nefer', 'Raiden']
s_tier = "DPS characters I own include: %s." %(genshin_DPS_Characters)

# Str.format

name = 'Frank'
birthday = '24\\04\\2003'
origin = 'Lagos'
new_strw = 'I am {}. I was born {}. I am from {}' .format(name, birthday, origin)

x = 200
y = 13
('{} + {} = {:.3f}'.format(x, y, x / y))

# F-Strings
a = 10
b = 3
(f'{a} / {b} = {a / b:.2f}')

# String Methods

'''
- Split, Strip, Join
- Upper, Lower, Title, Capitalize
- Replace, Find, rfind
- Indexing[], Count, 
'''
company = 'You cannot end a sentence with because because because is a conjunction'
print(company.rfind('because'))

Business = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
(Business.split())

quote = 'Codiing For All'
(quote[-1])

company = "Coding for all"
acronym = "".join(word[0].upper() for word in company.split())
(acronym)