# ==========================================================
# DECORATORS
# ==========================================================

# Decorator means:
# Add extra functionality to a function
# without modifying the original function.


def decorator(func):

    def wrapper():
        print("Before Function")

        func()

        print("After Function")

    return wrapper


@decorator
def greet():
    print("Hello Rajat")


greet()


# ==========================================================
# SUMMARY
# ==========================================================

# Decorator
# -> Adds extra functionality

# Wrapper Function
# -> Executes additional code

# @decorator_name
# -> Shortcut syntax



# ==========================================================
# *ARGS
# ==========================================================

# *args means:
# Accept multiple positional arguments.

def add(*args):

    total = 0

    for num in args:
        total += num

    print(total)


add(10, 20, 30, 40)


# ==========================================================
# SUMMARY
# ==========================================================

# *args
# -> Variable number of arguments

# Stored As
# -> Tuple

# Use When
# -> Number of inputs is unknown

# ==========================================================
# **KWARGS
# ==========================================================

# **kwargs means:
# Accept multiple keyword arguments.


def student(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)


student(
    name="Rajat",
    age=21,
    city="Noida"
)


# ==========================================================
# SUMMARY
# ==========================================================

# **kwargs
# -> Variable keyword arguments

# Stored As
# -> Dictionary

# Use When
# -> Parameter names are unknown


# ==========================================================
# LAMBDA FUNCTION
# ==========================================================

# Lambda means:
# Anonymous one-line function.


square = lambda x: x * x

print(square(5))


# ==========================================================
# SUMMARY
# ==========================================================

# Lambda Function
# -> One-line function

# Anonymous
# -> No function name required

# Mostly Used With
# -> map()
# -> filter()


# ==========================================================
# LIST COMPREHENSION
# ==========================================================

# List Comprehension means:
# Creating a list in a single line.


numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]

print(squares)


# ==========================================================
# SUMMARY
# ==========================================================

# List Comprehension
# -> Creates Lists

# Syntax
# -> [expression for item in iterable]

# Advantage
# -> Short and Readable


# ==========================================================
# SET COMPREHENSION
# ==========================================================

# Set Comprehension means:
# Creating a set in a single line.


numbers = [1, 2, 2, 3, 3, 4, 5]

unique_numbers = {num for num in numbers}

print(unique_numbers)


# ==========================================================
# SUMMARY
# ==========================================================

# Set Comprehension
# -> Creates Sets

# Removes
# -> Duplicate Values Automatically

# Syntax
# -> {expression for item in iterable}


# ==========================================================
# DICTIONARY COMPREHENSION
# ==========================================================

# Dictionary Comprehension means:
# Creating a dictionary in a single line.


numbers = [1, 2, 3, 4, 5]

square_dict = {
    num: num * num
    for num in numbers
}

print(square_dict)


# ==========================================================
# SUMMARY
# ==========================================================

# Dictionary Comprehension
# -> Creates Dictionaries

# Syntax
# -> {key:value for item in iterable}

# Output
# -> Key Value Pairs


# ==========================================================
# MAP FUNCTION
# ==========================================================

# map() means:
# Apply a function on every element.


numbers = [1, 2, 3, 4, 5]


def square(num):
    return num * num


result = list(map(square, numbers))

print(result)


# ==========================================================
# SUMMARY
# ==========================================================

# map()
# -> Applies Function To Every Element

# Returns
# -> Map Object

# Usually Convert Using
# -> list()


# ==========================================================
# FILTER FUNCTION
# ==========================================================

# filter() means:
# Keep only elements that satisfy a condition.


numbers = [1, 2, 3, 4, 5, 6]


def is_even(num):
    return num % 2 == 0


result = list(filter(is_even, numbers))

print(result)


# ==========================================================
# SUMMARY
# ==========================================================

# filter()
# -> Filters Elements

# Condition True
# -> Keep Element

# Condition False
# -> Remove Element


# ==========================================================
# ITERATORS
# ==========================================================

# Iterator means:
# An object that returns elements one by one.

# Every Iterator has two methods:
#
# __iter__() -> Returns the iterator object itself
# __next__() -> Returns the next element


# ==========================================================
# BUILT-IN ITERATOR EXAMPLE
# ==========================================================

numbers = [10, 20, 30]

# Create an iterator from a list
itr = iter(numbers)

print(next(itr))   # 10
print(next(itr))   # 20
print(next(itr))   # 30

# print(next(itr)) # StopIteration -> no more elements


# ==========================================================
# CUSTOM ITERATOR
# ==========================================================

# We can build our own iterator using a class.

class CountUp:

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


counter = CountUp(1, 5)

for num in counter:
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5


# ==========================================================
# SUMMARY
# ==========================================================

# Iterator
# -> Returns elements one by one

# iter()
# -> Creates an iterator

# next()
# -> Fetches next element

# StopIteration
# -> Raised when no more elements

# __iter__() + __next__()
# -> Required for custom iterators


# ==========================================================
# GENERATORS
# ==========================================================

# Generator means:
# A function that yields values one at a time
# instead of returning all values at once.

# Uses yield keyword instead of return.

# Advantage:
# Memory efficient -> values generated on demand.
# Does not store all values in memory at once.


# ==========================================================
# BASIC GENERATOR
# ==========================================================

def count_up(start, end):

    while start <= end:
        yield start       # Pauses here, returns value
        start += 1        # Resumes from here next time


gen = count_up(1, 5)

print(next(gen))   # 1
print(next(gen))   # 2
print(next(gen))   # 3

# Or use a for loop
for num in count_up(1, 5):
    print(num)


# ==========================================================
# RETURN VS YIELD
# ==========================================================

# return
# -> Function ends, all data returned at once

# yield
# -> Function pauses, one value returned at a time
# -> Function resumes from where it paused


# ==========================================================
# GENERATOR EXAMPLE: SQUARES
# ==========================================================

def squares(n):
    for i in range(1, n + 1):
        yield i * i


for val in squares(5):
    print(val)

# Output:
# 1
# 4
# 9
# 16
# 25


# ==========================================================
# GENERATOR EXPRESSION
# ==========================================================

# Like list comprehension but with ()
# Does not store values in memory.

gen = (num * num for num in range(1, 6))

for val in gen:
    print(val)


# ==========================================================
# GENERATOR VS LIST — MEMORY COMPARISON
# ==========================================================

import sys

normal_list = [num * num for num in range(1000)]
generator   = (num * num for num in range(1000))

print(sys.getsizeof(normal_list))   # Much larger (bytes)
print(sys.getsizeof(generator))     # Very small (bytes)

# Generator wins when dealing with large data.


# ==========================================================
# REAL LIFE USE CASE OF GENERATORS
# ==========================================================

# Reading a large file line by line
# without loading entire file into memory.

def read_large_file(filepath):
    with open(filepath, "r") as file:
        for line in file:
            yield line.strip()

# Used in ML pipelines for large datasets.


# ==========================================================
# SUMMARY
# ==========================================================

# Generator
# -> Function with yield

# yield
# -> Pauses function, returns one value

# Memory Efficient
# -> Values produced on demand

# Generator Expression
# -> (expression for item in iterable)

# Use Cases
# -> Large files
# -> Infinite sequences
# -> ML data pipelines


# ==========================================================
# ITERATOR VS GENERATOR — QUICK COMPARISON
# ==========================================================

# Feature         | Iterator (Class)    | Generator (Function)
# ----------------|---------------------|---------------------
# Defined Using   | Class               | Function with yield
# Methods Needed  | __iter__, __next__  | Only yield
# Memory          | Manual management   | Auto, lazy loading
# Code Length     | More verbose        | Short and clean
# Use When        | Complex logic       | Simple sequences