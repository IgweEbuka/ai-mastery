"""
- Python is an object oriented programming language.
- Everything in python is an object with properties and methods.
- A class is an object constructor.
- The class defines the behaviour of the object while the object represents the class.
- To create a class we use the class keyword and a column. It follows CamelCase laws.
- To create an object we call the class.
- Class Constructor:
    A class without a constructor is not really useful in real applications.
    The init constructor function has self parameter which is a reference to the current instance of the class.
- Objects can have methods. The methods are functions which belong to the object.
    These methods are defined under the constructor function.
    These methods can be dot called to act on an already created object.
    Sometimes you will want your methods to have default values and that is possible.
- Modifying methods:
    So within the class. Define a method that takes self and the change you want made to it.
    Then like before dot call the method on the existing object.
- Inheritance:
    Inheritance allows us to define a class that inherits all the methods and properties from parent class.
    The parent class gives all the methods and properties.
    The child class inherits from the parents.
- Overriding a parent:
    If we do call the constructor we can access the parent properties by calling super.
        i.e. super().__init__(attributes of parent class).
    From here you can add a new method to the child or override the existing methods of the parent.
    When we add the init() function, the child class will no longer inherit the parent's init() function.
"""

# Creating a class
class RiceAndBeans:
    pass

# Creating an object
p = RiceAndBeans()
    # print(p)

# Class Constructor

class Person:
    def __init__(self, name, age, gender,country,city):
        self.name = name
        self.age = age
        self.gender = gender
        self.country = country
        self.city = city
        self.skills = []


    def person_info(self):
        if self.gender.lower() == "female":
            return f"{self.name} is from {self.country} and stays in {self.city}. She is a currently {self.age}."
        else:
            return f"{self.name} is from {self.country} and stays in {self.city}. He is a currently {self.age}."

    def add_skills(self, skill):
        self.skills.append(skill)

class Student(Person):
    pass

s1 = Student("Ebuka", 23, "Male", "Nigeira", "PH")
s1.add_skills("Coding")
s1.add_skills("Gaming")
s2 = Student("Ella", 20, "Female", "Nigeria", "PH")

# print(s1.person_info())
# print(s1.skills)
# print(s2.person_info())
# print(s2.skills)
        

p1 = Person("Sonia", 20, "Female", "Nigeria", "PH")
p2 = Person("Jake", 23, "Male", "America", "Florida")

# print(p1.person_info())
# print(p2.person_info())

class Human(Person):
    def __init__(self, name, age, gender, country, city, height):
        self.height = height 
        super().__init__(name, age, gender, country, city)
    def person_info(self):
        height = "Tall" if self.height >= 100 else "Short"
        return f"{self.name} is a {height} {self.gender}."

h1 = Human('Precious', 20, "Female", "Finland", "Helsinki", 85)
print(h1.person_info())

#