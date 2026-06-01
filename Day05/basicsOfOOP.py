# ==========================================================
# OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON
# ==========================================================

# Programming Paradigms:
# 1. Imperative Programming  -> Focus on HOW to do things
# 2. Functional Programming  -> Focus on functions
# 3. Object Oriented Programming (OOP) -> Focus on objects

# OOP is based on the concept of:
# - Classes
# - Objects
# - Attributes
# - Methods
# - Constructors
# - Encapsulation
# - Inheritance
# - Polymorphism
# - Abstraction


# ==========================================================
# 1. CLASSES
# ==========================================================

# A Class is a blueprint/template used to create objects.

# Real-Life Example:
# Blueprint  -> House Design
# Object     -> Actual House

class Factory:

    # Class Attribute
    a = 12

    # Instance Method
    def hello(self):
        print("Hello, how are you?")

    # This line executes when the class is created
    print("Factory class is getting initialized...")


# ==========================================================
# 2. OBJECTS
# ==========================================================

# Object = Instance of a Class

# Creating an object
obj = Factory()

# Accessing class attribute
print(obj.a)

# Calling method
obj.hello()

# Directly using temporary object
print(Factory().a)
Factory().hello()


# ==========================================================
# WHAT IS SELF?
# ==========================================================

# self refers to the current object.

# When we write:
#
# obj.hello()
#
# Python internally does:
#
# Factory.hello(obj)
#
# Therefore one argument is automatically passed.
# To receive that argument, we use self.

# Example:

class Student:

    def show(self):
        print(self)


s1 = Student()
s1.show()

# Output:
# <__main__.Student object at 0x...>


# ==========================================================
# 3. CONSTRUCTORS
# ==========================================================

# Constructor is a special method that runs automatically
# whenever an object is created.

# Constructor Name:
# __init__()

# __init__ is called a Dunder Method
# (Double Underscore Method)


class Organization:

    # Constructor
    def __init__(self, material, zips, pockets):

        # Instance Attributes
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(
            f"Material = {self.material}, "
            f"Zips = {self.zips}, "
            f"Pockets = {self.pockets}"
        )


# Creating Objects

reebok = Organization("Leather", 3, 2)
campus = Organization("Nylon", 3, 3)

# Accessing Instance Attributes

print(campus.pockets)
print(reebok.material)

# Calling Method

reebok.show()
campus.show()


# ==========================================================
# REAL LIFE EXAMPLE OF CONSTRUCTOR
# ==========================================================

class Car:

    def __init__(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display(self):
        print(
            f"Company = {self.company}, "
            f"Model = {self.model}, "
            f"Price = ₹{self.price}"
        )


car1 = Car("Hyundai", "i20", 900000)
car2 = Car("Honda", "City", 1500000)

car1.display()
car2.display()


# ==========================================================
# 4. TYPES OF ATTRIBUTES
# ==========================================================

class Animal:

    # Class Attribute
    # Shared among all objects

    name = "Lion"

    # Constructor
    def __init__(self, age):

        # Instance Attribute
        # Different for each object

        self.age = age

    # Instance Method
    def show(self):
        print("How are you?")

    # Class Method
    @classmethod
    def hello(cls):
        print("How are you, my friend!!")

    # Static Method
    @staticmethod
    def static():
        print("Who are you?")


obj = Animal(12)

# Accessing Instance Attribute
print(obj.age)

# Accessing Class Attribute
print(obj.name)

# Calling Instance Method
obj.show()

# Calling Class Method
Animal.hello()

# Calling Static Method
Animal.static()


# ==========================================================
# CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE
# ==========================================================

class Employee:

    # Class Attribute
    company = "Google"

    def __init__(self, name):
        self.name = name


e1 = Employee("Rajat")
e2 = Employee("Aman")

print(e1.company)
print(e2.company)

print(e1.name)
print(e2.name)

# company is shared
# name is different for each object


# ==========================================================
# 5. INSTANCE METHODS
# ==========================================================

# Instance Methods work with object data.

class Person:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")


p1 = Person("Rajat")
p1.greet()


# ==========================================================
# 6. CLASS METHODS
# ==========================================================

# Class Methods work with Class Attributes.

class College:

    college_name = "Galgotias College"

    @classmethod
    def display_college(cls):
        print(cls.college_name)


College.display_college()


# ==========================================================
# 7. STATIC METHODS
# ==========================================================

# Static Methods neither use:
# self
# nor
# cls

# Used for utility/helper functions.

class Math:

    @staticmethod
    def add(a, b):
        return a + b


print(Math.add(10, 20))


# ==========================================================
# SUMMARY
# ==========================================================

# Class
# -> Blueprint for creating objects

# Object
# -> Instance of a class

# Attribute
# -> Variables inside a class

# Method
# -> Functions inside a class

# Constructor (__init__)
# -> Automatically executes when object is created

# self
# -> Refers to current object

# Class Attribute
# -> Shared among all objects

# Instance Attribute
# -> Unique for each object

# Instance Method
# -> Uses self

# Class Method
# -> Uses cls

# Static Method
# -> Uses neither self nor cls