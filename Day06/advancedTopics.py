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

