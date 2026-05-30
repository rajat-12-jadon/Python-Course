# Functions in Python group reusable code into a block that can be executed
# by calling the function name. This helps avoid repetition and makes program
# modular and readable.

#Positional Arguments
def greet():
    print("Hello Everyone")

greet()

def addition(a, b):
    print(f"sum of two numbers is {a + b}")

addition(6, 8)
addition(7, 393)


#Default Arguments

def hello(name, age = 22):
    print(f"Your name is {name} and age is {age}")

hello("Rajat")
hello("Rajat", 25) #override the default age

#Keyword Arguments

def greet(name, age):
    print(name, age) #22 Rajat -> order matters -> positional argument

greet(22, "Rajat")
greet(age=22, name="Rajat") # order doesn't matter as keywords use

def palindrome(str):
    rev = ""

    for i in range(len(str) - 1, -1, -1):
        rev = rev + str[i]
    
    if rev == str:
        print("Palindrome")
    else:
        print("Not a palindrome")

palindrome("naman")
palindrome("Naman")
palindrome("malayalam")


#return and print -> print already covered

def hello():
    return "Hello everyone" #-> return output on the line of code where you call function 

print(hello())