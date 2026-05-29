# 1. if-else statement

age = 10

if age >= 18 :
    print("You are eligible for vote.")
else :
    print("Not eligible")

# 2. if-elif-else

if age < 20 :
    print("You are teenager.")
elif age >= 20 and age < 60 : 
    print("You are an adult.")
else :
    print("You are a senior citizen.")

# 3. if-elif-elif...-else

if age < 13 :
    print("You are a child.")
elif age >=13 and age < 20 :
    print("You are teenager.")
elif age >= 20 and age < 60 : 
    print("You are an adult.")
else :
    print("You are a senior citizen.")


# 4. nested if

num = 12

if num >= 0:
    print("The number is positive.")
    
    # Nested if
    if num % 2 == 0:
        print("It is also an even number.")
    else:
        print("It is an odd number.")
else:
    print("The number is negative.")

    
# Questions Practice:

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

if a > b :
    print(a)
else :
    print(b)

gender = input("Enter your gender (M/F) or (m/f): ")

if gender == 'F' or gender == 'f' :
    print("Good morning ma'am.")
else :
    print("Good morning Sir.")

if a % 2 == 0 :
    print("Even")
else :
    print("Odd")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18 :
    print(f"Hello {name}, you are eligible for vote.")
else :
    print(f"Hello {name}, you are not eligible for vote.")


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Temperature Analysis

temp = int(input("Enter the degree of temperature: "))

if temp < 0 :
    print("Freezing Cold❄️")
elif temp >= 0 and temp < 10 :
    print("Very Cold🥶")
elif temp >= 10 and temp < 20 :
    print("Cold🌫️")
elif temp >= 20 and temp < 30 :
    print("Pleasant⛅️")
elif temp >= 30 and temp < 40 :
    print("Hot🔥")
else :
    print("Very Hot🥵")