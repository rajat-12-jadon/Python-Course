# Dunder Methods

# Dunder methods are special methods in Python that start and end with 
# double underscores, like __init__, __str__, __add__, etc

# They automatically get called when you perform certain actions on an object.

# They help you:
        # customize behavious of your class
        # make your class objects behave like built-in data types (like strings, lists, etc.)


# ==========================================================
# DUNDER (MAGIC) METHODS IN PYTHON
# ==========================================================

# Dunder = Double Underscore

# Dunder Methods are special methods whose names start
# and end with double underscores (__).

# Examples:
#
# __init__()
# __str__()
# __len__()
# __add__()
# __sub__()
#
# Python automatically calls them when certain actions
# are performed on objects.

# They help us:
#
# 1. Customize the behavior of our classes
# 2. Make objects behave like built-in data types
# 3. Support operators (+, -, *, etc.)


# ==========================================================
# 1. __init__()
# ==========================================================

# Constructor
# Called automatically when an object is created.

class Student:

    def __init__(self, name):
        self.name = name


obj = Student("Rajat")

print(obj.name)

print()


# ==========================================================
# 2. __str__()
# ==========================================================

# Controls what gets printed when we print an object.

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student Name = {self.name}"


obj = Student("Rajat")

print(obj)

# Internally:
#
# print(obj)
#
# becomes:
#
# print(obj.__str__())

print()


# ==========================================================
# WITHOUT __str__()
# ==========================================================

class Test:
    pass


obj = Test()

print(obj)

# Output Similar To:
#
# <__main__.Test object at 0x12345>

# Not user friendly.

print()


# ==========================================================
# 3. __len__()
# ==========================================================

# Controls what happens when len() is used.

class Student:

    def __init__(self, subjects):
        self.subjects = subjects

    def __len__(self):
        return len(self.subjects)


obj = Student(
    ["Maths", "Science", "English"]
)

print(len(obj))

# Internally:
#
# len(obj)
#
# becomes:
#
# obj.__len__()

print()


# ==========================================================
# 4. __add__()
# ==========================================================

# Controls + operator.

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


n1 = Number(10)
n2 = Number(20)

print(n1 + n2)

# Internally:
#
# n1 + n2
#
# becomes:
#
# n1.__add__(n2)

print()


# ==========================================================
# 5. __sub__()
# ==========================================================

# Controls - operator.

class Number:

    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value


n1 = Number(50)
n2 = Number(20)

print(n1 - n2)

print()


# ==========================================================
# 6. __mul__()
# ==========================================================

# Controls * operator.

class Number:

    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value * other.value


n1 = Number(5)
n2 = Number(4)

print(n1 * n2)

print()


# ==========================================================
# 7. __truediv__()
# ==========================================================

# Controls / operator.

class Number:

    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        return self.value / other.value


n1 = Number(20)
n2 = Number(5)

print(n1 / n2)

print()


# ==========================================================
# 8. __eq__()
# ==========================================================

# Controls == operator.

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks


s1 = Student(90)
s2 = Student(90)

print(s1 == s2)

print()


# ==========================================================
# 9. __lt__()
# ==========================================================

# Controls < operator.

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student(80)
s2 = Student(90)

print(s1 < s2)

print()


# ==========================================================
# 10. __gt__()
# ==========================================================

# Controls > operator.

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


s1 = Student(95)
s2 = Student(80)

print(s1 > s2)

print()


# ==========================================================
# REAL LIFE EXAMPLE
# ==========================================================

class Product:

    def __init__(self, name, price):

        self.name = name
        self.price = price

    def __str__(self):

        return (
            f"Product(Name={self.name}, "
            f"Price=₹{self.price})"
        )

    def __add__(self, other):

        return self.price + other.price


p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1000)

print(p1)

print(p1 + p2)

print()


# ==========================================================
# SUMMARY
# ==========================================================

# __init__()
# -> Constructor

# __str__()
# -> String Representation

# __len__()
# -> len(object)

# __add__()
# -> +

# __sub__()
# -> -

# __mul__()
# -> *

# __truediv__()
# -> /

# __eq__()
# -> ==

# __lt__()
# -> <

# __gt__()
# -> >

# Dunder Methods allow us to customize how
# objects behave with operators and functions.



# Easy Memory Tricks


# print(obj)   → __str__()

# len(obj)     → __len__()

# obj1 + obj2  → __add__()

# obj1 - obj2  → __sub__()

# obj1 * obj2  → __mul__()

# obj1 / obj2  → __truediv__()

# obj1 == obj2 → __eq__()

# obj1 < obj2  → __lt__()

# obj1 > obj2  → __gt__()