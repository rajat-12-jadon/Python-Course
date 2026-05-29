# to check unicode of any value --> use ord();

s = "A"
print(ord(s))

t = 65
print(chr(t)) #to find the character original value from unicode

# Indexing in String

a = "Hello World"
# H e l l o   W o r l d
# 0 1 2 3 4 5 6 7 8 9 10
#  H   e   l  l  o     W  o  r  l  d
# -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(a[0])
print(a[-1])
print(a[-11])

# String Slicing

# a[start : stop : steps] --> stop (not include)
print(a[0 : 5 : 1])


#Type Conversions

# Explicit Type Conversion

# functions use for conversion -> int(), float(), str(), and bool()

x = 12
print(type(x))
x = str(12)
print(type(x))

# for convert value from strings to int or float, value should be in number form

# any value convert into bool gives truthy value except 7: 
# these are False, 0, 0.0, "", [], {}, () -> (), [], {} - must be empty

a = [1, 2, 3]
print(bool(a))


#Implicit Type Conversions

a = 12 #integer

print(a/3) #float

name = "Rajat"
age = 22

# Normal String
print("My name is",name, "and I am",age, "years old.")

# Formatted String
print(f"My name is {name} and I am {age} years old")


userName = input("Enter your name: ")
userAge = input("Enter your age: ")
print(type(userAge)) # class <str> but need int, so type conversion

userAge = int(input("Enter your age: "))
print(type(userAge)) # class <int>

print(f"User name is {userName} and he is {userAge} years old")