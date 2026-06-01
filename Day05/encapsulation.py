# Encapsulation

# ==========================================================
# ABSTRACTION
# ==========================================================

# Abstraction means:
# Showing only essential information
# and hiding implementation details.

# Real Life Example:
# TV Remote
# ATM Machine
# Car Steering

# Python provides Abstraction through:
#
# ABC
# abstractmethod

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


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
# SUMMARY
# ==========================================================

# Encapsulation
# -> Hides Data

# Abstraction
# -> Hides Implementation

# ABC
# -> Abstract Base Class

# @abstractmethod
# -> Method that MUST be implemented
#    by child classes.