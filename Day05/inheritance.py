# ==========================================================
# INHERITANCE IN PYTHON
# ==========================================================

# Inheritance allows one class to acquire the properties
# (attributes and methods) of another class.

# Parent Class / Super Class
# Child Class / Sub Class

# Benefits:
# 1. Code Reusability
# 2. Less Code Duplication
# 3. Easier Maintenance


# ==========================================================
# 1. SINGLE INHERITANCE
# ==========================================================

# One Child Class inherits from One Parent Class

class FactoryMumbai:  # Parent Class

    # Class Attribute
    city = "Mumbai"

    # Method
    def hello(self):
        print("I am a method of the parent class.")


# Child Class
class FactoryPune(FactoryMumbai):
    pass


# Parent Object
obj = FactoryMumbai()

print(obj.city)
obj.hello()

print()

# Child Object
obj2 = FactoryPune()

# Child can access parent's attributes and methods
print(obj2.city)
obj2.hello()


# ==========================================================
# CONSTRUCTORS IN INHERITANCE
# ==========================================================

# If Child Class does not have its own constructor,
# Parent Class constructor is automatically used.


class Animal:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Hello, your name is {self.name}")


class Human(Animal):
    pass


animal1 = Animal("Lion")
person1 = Human("Rajat")

animal1.show()
person1.show()


# ==========================================================
# CHILD CLASS WITH ITS OWN CONSTRUCTOR
# ==========================================================

# When Child has its own constructor,
# Parent constructor is NOT called automatically.

# Use super().__init__() to call Parent Constructor.


class Animal:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Hello, your name is {self.name}")


class Human(Animal):

    def __init__(self, name, age):

        # Calling Parent Constructor
        super().__init__(name)

        self.age = age

    def show(self):
        print(
            f"Hello, your name is {self.name} "
            f"and you are {self.age} years old."
        )


animal1 = Animal("Mufasa")
person1 = Human("Rajat", 23)

animal1.show()
person1.show()


# ==========================================================
# TYPES OF INHERITANCE
# ==========================================================


# ==========================================================
# 2. MULTIPLE INHERITANCE
# ==========================================================

# One Child inherits from Multiple Parent Classes

class Animal:
    name1 = "Lion"


class Human:
    name2 = "Harsh"


class Robot(Animal, Human):
    name3 = "Charlie123"


obj = Robot()

print(obj.name1)
print(obj.name2)
print(obj.name3)


# ==========================================================
# MRO (METHOD RESOLUTION ORDER)
# ==========================================================

# Python searches for methods and constructors
# according to MRO.

class Animal:

    def __init__(self, name):
        print("Animal Constructor Called")


class Human:

    def __init__(self, name, age):
        print("Human Constructor Called")


class Robot(Animal, Human):
    pass


obj = Robot("Lion")

# Human Constructor is NOT called.

# Why?

# MRO:
# Robot -> Animal -> Human -> object

print(Robot.__mro__)


# ==========================================================
# MULTIPLE INHERITANCE WITH BOTH CONSTRUCTORS
# ==========================================================

class Animal:

    def __init__(self, name):
        self.name = name
        print("Animal Constructor")


class Human:

    def __init__(self, name, age):
        self.age = age
        print("Human Constructor")


class Robot(Animal, Human):

    def __init__(self, name, age):

        # Calling both constructors manually
        Animal.__init__(self, name)
        Human.__init__(self, name, age)


obj = Robot("Rajat", 23)


# ==========================================================
# 3. MULTI-LEVEL INHERITANCE
# ==========================================================

# Grandparent -> Parent -> Child

class Factory:

    def __init__(self, material, zips):
        self.material = material
        self.zips = zips


class BhopalFactory(Factory):

    def __init__(self, material, zips, color):

        super().__init__(material, zips)

        self.color = color


class PuneFactory(BhopalFactory):

    def __init__(self, material, zips, color, pockets):

        super().__init__(material, zips, color)

        self.pockets = pockets

    def show(self):
        print(
            f"Material : {self.material}\n"
            f"Zips     : {self.zips}\n"
            f"Color    : {self.color}\n"
            f"Pockets  : {self.pockets}"
        )


bag = PuneFactory(
    "Leather",
    3,
    "Black",
    4
)

bag.show()


# ==========================================================
# 4. HIERARCHICAL INHERITANCE
# ==========================================================

# One Parent -> Multiple Children

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


class Cat(Animal):

    def meow(self):
        print("Cat meows")


dog = Dog()

dog.sound()
dog.bark()

print()

cat = Cat()

cat.sound()
cat.meow()


# ==========================================================
# 5. HYBRID INHERITANCE
# ==========================================================

# Combination of Multiple + Multilevel Inheritance

class A:

    def showA(self):
        print("Class A")


class B(A):

    def showB(self):
        print("Class B")


class C(A):

    def showC(self):
        print("Class C")


class D(B, C):

    def showD(self):
        print("Class D")


obj = D()

obj.showA()
obj.showB()
obj.showC()
obj.showD()


# ==========================================================
# SUMMARY
# ==========================================================

# Single Inheritance
# Parent -> Child

# Multiple Inheritance
# Parent1 + Parent2 -> Child

# Multi-Level Inheritance
# Grandparent -> Parent -> Child

# Hierarchical Inheritance
# Parent -> Child1, Child2, Child3

# Hybrid Inheritance
# Combination of Multiple Types

# super()
# -> Calls Parent Class Methods/Constructors

# MRO
# -> Method Resolution Order
# -> Defines the order Python follows while
#    searching for methods and constructors.

# Check MRO using:
#
# print(ClassName.__mro__)
#
# Example:
#
# print(Robot.__mro__)