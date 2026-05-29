# 1. Arithmetic Operations

# +, -, *, /, %, //, **

a = 12
b = 10

print(a + b) # 22
print( a- b) # 2
print(a * b) # 120
print(a / b) # 1.2
print(a % b) # 2
print(a // b) # 1
print(a ** b) # 61917364224  

# 2. Assignment Operator -> =

a = 10 # 10 is assigned to a

# Compound Assignment Operations
# +=, -=, *=, /=, //=, %=, **=

x = 2

x += 5
print(x)

x -= 5
print(x)

x *= 5
print(x)

x /= 5
print(x)

x = 15

x //= 5
print(x)

x %= 5
print(x)

x **= 5
print(x)

# 3. Comparison Operators

# ==, >=, <=, !=, >, <

m = 10
n = 8

print(m == n)
print(m != n)
print(m > n)
print(m < n)
print(m >= n)
print(m <= n)

x = "A"
y = "B"

# also can be used in string

print(x > y)
print(x < y)
print(x != y)

# 4. Logical Operators

# and, or, not

print(134 <= 432 and 34 == 34) # comparisons ke beech me logic lagana

print(True or False)
print(True and True)
print(not True)

print(5 or 7) # concept or short circuiting

# if use 'or' -> check first value and if first value is truthy return it, if not then return second value
# if use 'and' -> if first value is falsy return it, if not then return second value

print(5 and 7)
print(0 and 3)
print(1 and 3)
print(0 or 7)


print("Homework Questions: ")

print(True and False) # False
print(126 > 130) # False
print((456 == 456) != (235 == 236)) # True
print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13) # True
print(True and bool(0)) # False