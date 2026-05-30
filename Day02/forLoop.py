import math
# #print "hello world" 100th times manually can be inefficient and takes 100 lines of code.

# #using loop make it 2 lines of code

# for i in range(1, 21, 1) :   # range(start, end, steps) -> end is not included
#     print("Hello World")

# for i in range(20): 
#     print(i) #print from 0 to 19, as by default it starts from 0

# for i in range(16, 0, -1): 
#     print(i)  #in reverse order

# for i in range(-3, -16, -1) :
#     print(i)

# for i in range(5, 51, 5): 
#     print(i) #table of 5 using range

# for i in range(1, 11, 1):
#     print(f"5 * {i} = {i*5}") # efficient way to print

# # n = int(input("Enter number: ")) #take input from user

# # for i in range(1, 11, 1):
# #     print(f"{n} * {i} = {n * i}")

# a = "Codeforces"

# for i in range(0, len(a), 1):
#     print(a[i], end=" ")

# print()

# b = "Everything is temporary"

# for i in b:
#     print(i, end = " ")

# print()

# #concept of break and continue

# for i in range(1, 21, 1):
#     if i == 15:
#         break
#     else:
#         print(i)

# for i in range(1, 21, 1):
#     if i % 2 != 0:
#         continue
#     else:
#         print(i)

# for i in range(1, 21, 1):
#     if i == 110:
#         print("Break statement is executed.")
#         break
#     print(i)

# else:
#     print("Break statement isn't executed.")

# Questions Practice

#1. Accept integer and print hello world n times

n = int(input("Enter number: "))

for i in range(n):
    print("hello world")

#2. print natural number upto n

for i in range(1, n+1, 1):
    print(i)

#3. reverse natural number n to 1

for i in range(n, 0, -1):
    print(i)

#4. print table of n

for i in range(1, 11, 1):
    print(f"{n} * {i} = {n * i}")

#5. sum up to n terms

sum = 0
for i in range(1, n + 1, 1):
    sum += i

print(sum)

#6. factorial of n

fact = 1
for i in range(n, 0, -1):
    fact *= i

print(fact)

#7. print sum of odd and even numbers in range upto n separately

evenSum = 0
oddSum = 0
for i in range(n):
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i
print(evenSum, oddSum)

#8. print all factors of a number

for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        print(i)
        if i != n // i:
            print(n // i)

#9. check if it's a perfect number or not

sumOfFactors = 0

for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        sumOfFactors += i
        if i != n // i:
            sumOfFactors += n // i

if sumOfFactors - n == n:
    print("Number is perfect.")
else:
    print("Not a perfect number.")

#10. check whether number is prime or not
count = 0
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        count += 1
        if i != n // i:
            count += 1

if count > 2:
    print("Not a prime number.")
else:
    print("Prime number.")
#11. reverse string
s = "malayalam"
t = ""
for i in range(len(s) - 1, -1, -1):
    t += (s[i])
print(t)
#12. check whether string is palindrome or not
if s == t:
    print("Palindrome.")
else:
    print("Not a palindrome.")
#13. count all letters, digits, special symbols from a given string separately

x = "44cy)PP(&P((*(&(*(^P^b;p0989ovtywt3qz4123r"

char = 0
digit = 0
symbol = 0
for i in x:
    if i.isalpha():
        char += 1
    elif i.isdigit():
        digit += 1
    else:
        symbol += 1

print(f"Count of characters is {char}, count of digits is {digit}, and count of symbols is {symbol}")