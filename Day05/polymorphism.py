# ==========================================================
# POLYMORPHISM IN PYTHON
# ==========================================================

# Poly = Many
# Morph = Forms

# Polymorphism means:
# One thing can take many forms.

# Examples:
# - Same method name behaves differently.
# - Same operator behaves differently.
# - Different objects respond to the same method.


# ==========================================================
# 1. METHOD OVERRIDING
# ==========================================================

# Method Overriding occurs when a child class provides
# its own implementation of a method already defined
# in the parent class.

# Parent Class

class Animal:

    def show(self):
        print("Hello, Lion")


# Child Class

class Human(Animal):

    # Overriding Parent Method
    def show(self):
        print("Hello, Rajat")


obj = Human()

# Child method is called instead of Parent method
obj.show()


# Output:
# Hello, Rajat


# ==========================================================
# ACCESSING PARENT METHOD AFTER OVERRIDING
# ==========================================================

# We can use super() to call Parent Method.

class Animal:

    def show(self):
        print("Hello, Lion")


class Human(Animal):

    def show(self):

        # Calling Parent Method
        super().show()

        print("Hello, Rajat")


obj = Human()

obj.show()


# Output:
# Hello, Lion
# Hello, Rajat


# ==========================================================
# REAL LIFE EXAMPLE OF METHOD OVERRIDING
# ==========================================================

class Shape:

    def area(self):
        print("Area Formula")


class Circle(Shape):

    def area(self):
        print("Area = πr²")


class Rectangle(Shape):

    def area(self):
        print("Area = Length × Breadth")


c = Circle()
r = Rectangle()

c.area()
r.area()


# ==========================================================
# 2. DUCK TYPING
# ==========================================================

# Duck Typing:
#
# "If it walks like a duck and quacks like a duck,
# then treat it as a duck."
#
# Python does not care about the object's type.
# It only cares whether the required method exists.

class Animal:

    def show(self):
        print("I am here")


class Human:

    def show(self):
        print("Hello, I am also here")


obj = Animal()
obj1 = Human()

obj.show()
obj1.show()


# ==========================================================
# DUCK TYPING EXAMPLE
# ==========================================================

# Function works with any object that has show()

def display(data):
    data.show()


class Animal:

    def show(self):
        print("Animal is present")


class Human:

    def show(self):
        print("Human is present")


display(Animal())
display(Human())


# Output:
# Animal is present
# Human is present


# ==========================================================
# DUCK TYPING FAILURE EXAMPLE
# ==========================================================

class Robot:

    def run(self):
        print("Robot is running")


# display(Robot())

# Error:
#
# AttributeError:
# 'Robot' object has no attribute 'show'
#
# Because Duck Typing only checks
# whether the required method exists.


# ==========================================================
# 3. OPERATOR OVERLOADING
# ==========================================================

# Same operator behaves differently
# depending on the data type.

print(10 + 20)

print("Rajat " + "Jadon")

print([1, 2] + [3, 4])


# Output:
# 30
# Rajat Jadon
# [1, 2, 3, 4]


# ==========================================================
# CUSTOM OPERATOR OVERLOADING
# ==========================================================

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)


# Output:
# 30


# ==========================================================
# 4. POLYMORPHISM USING SAME METHOD NAME
# ==========================================================

class Dog:

    def sound(self):
        print("Bark Bark")


class Cat:

    def sound(self):
        print("Meow Meow")


class Cow:

    def sound(self):
        print("Moo Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()


# Output:
# Bark Bark
# Meow Meow
# Moo Moo


# ==========================================================
# SUMMARY
# ==========================================================

# Polymorphism
# -> One thing, many forms

# Method Overriding
# -> Child class redefines Parent method

# Duck Typing
# -> Python checks methods, not object type

# Operator Overloading
# -> Same operator behaves differently

# Examples:
#
# +  -> Addition
# +  -> String Concatenation
# +  -> List Merging
#
# All are examples of Polymorphism.