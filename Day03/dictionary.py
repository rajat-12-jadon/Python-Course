# ==========================================
# Dictionary in Python
# ==========================================

# Properties of Dictionary:
#
# 1. Mutable
#    - We can add, update, or delete key-value pairs.
#
# 2. Ordered
#    - Dictionaries maintain insertion order (Python 3.7+).
#
# 3. Heterogeneous
#    - Keys and values can be of different data types.
#
# 4. Unique Keys
#    - Duplicate keys are NOT allowed.
#    - If the same key appears multiple times,
#      the last value overrides the previous value.
#
# 5. Duplicate Values Allowed
#    - Multiple keys can have the same value.


# ==========================================
# Creating a Dictionary
# ==========================================

d = {
    1: "Hello",
    2: 22,
    3: "Hello"
}

print(d)

# Accessing a value using a key
print(d[3])      # Output: Hello


# ==========================================
# Duplicate Keys
# ==========================================

d1 = {
    1: "hello",
    1: "Everyone"
}

# The second value overrides the first one
print(d1)

print(d1[1])     # Output: Everyone


# ==========================================
# Creating Another Dictionary
# ==========================================

d2 = {
    1: 10,
    2: 20,
    3: 30,
    4: 40
}

print(d2)


# ==========================================
# Updating Existing Key
# ==========================================

d2[1] = 25

print(d2)


# ==========================================
# Adding New Key using update()
# ==========================================

d2.update({50: 500})

print(d2)


# ==========================================
# Adding New Key using Assignment
# ==========================================

d2[55] = 600

print(d2)


# ==========================================
# Deleting Key-Value Pair
# ==========================================

del d2[3]

print(d2)


del d2[55]

print(d2)


# ==========================================
# Traversing Dictionary
# ==========================================

print("\nKeys:")

for i in d2:
    print(i)

# Same as:
# for i in d2.keys():
#     print(i)


# ==========================================
# Printing Values
# ==========================================

print("\nValues:")

for i in d2:
    print(d2[i])


# ==========================================
# Printing Key and Value
# ==========================================

print("\nKey and Value:")

for i in d2:
    print(i, d2[i])


# ==========================================
# Using items()
# ==========================================

print("\nItems:")

for i in d2.items():
    print(i)

# Output:
# (1, 25)
# (2, 20)
# ...


# ==========================================
# Unpacking Key and Value
# ==========================================

print("\nUsing items() with unpacking:")

for key, value in d2.items():
    print(key, value)


# ==========================================
# Using values()
# ==========================================

print("\nValues using values():")

for value in d2.values():
    print(value)


# ==========================================
# Using keys()
# ==========================================

print("\nKeys using keys():")

for key in d2.keys():
    print(key)


# ==========================================
# Clearing Dictionary
# ==========================================

d2.clear()

print("\nAfter clear():")
print(d2)


# ==========================================
# Empty Dictionary
# ==========================================

print(type({}))      # dict

# Empty Set
print(type(set()))   # set


#=========================================
# Deep Copy vs Shallow Copy
#=========================================

# attached in .md file, refer that file

d1 = {
    2: 10,
    4: 23,
    5: 34,
    6: 21
}

d2 = {
    1: 10,
    2: 20,
    3: 30,
    4: 40
}

print(d2.items())


# ==========================================
# Dictionary Practice Questions
# ==========================================

# Original Dictionaries

d1 = {
    2: 10,
    4: 23,
    5: 34,
    6: 21
}

d2 = {
    1: 10,
    2: 20,
    3: 30,
    4: 40
}

# ==========================================
# Question 1
# Merge Two Dictionaries
# ==========================================

# Create a copy so original d1 remains unchanged

merged_dict = d1.copy()

# Add all key-value pairs from d2

for key in d2:
    merged_dict[key] = d2[key]

print("Merged Dictionary:")
print(merged_dict)

# Output:
# {
#     2: 20,
#     4: 40,
#     5: 34,
#     6: 21,
#     1: 10,
#     3: 30
# }

print()


# ==========================================
# Question 2
# Sum of All Values in Dictionary
# ==========================================

total = 0

for value in d2.values():
    total += value

print("Sum of Values:")
print(total)

# Output:
# 100

print()


# ==========================================
# Question 3
# Count Frequency of Elements in List
# ==========================================

a = [1, 2, 3, 2, 2, 1, 2, 1, 1, 3, 4, 4, 3, 5, 6, 7]

freq = {}

for num in a:

    # If number already exists
    if num in freq:
        freq[num] += 1

    # First occurrence
    else:
        freq[num] = 1

print("Frequency Dictionary:")
print(freq)

# Output:
# {
#     1: 4,
#     2: 4,
#     3: 3,
#     4: 2,
#     5: 1,
#     6: 1,
#     7: 1
# }

print()


# ==========================================
# Question 4
# Combine Two Dictionaries
# Add Values of Common Keys
# ==========================================

# Recreate original dictionary
# because dictionaries are mutable

d1 = {
    2: 10,
    4: 23,
    5: 34,
    6: 21
}

combined_dict = d1.copy()

for key in d2:

    # Common key
    if key in combined_dict:
        combined_dict[key] += d2[key]

    # New key
    else:
        combined_dict[key] = d2[key]

print("Combined Dictionary:")
print(combined_dict)

# Output:
# {
#     2: 30,
#     4: 63,
#     5: 34,
#     6: 21,
#     1: 10,
#     3: 30
# }