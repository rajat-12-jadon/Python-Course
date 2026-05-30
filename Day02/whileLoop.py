# to run loop for a specific condition

a = 1

while a <= 30:
    print(a)
    a = a + 1

#Questions practice

#1. Print all digits of a number

n = int(input("Enter your number: "))
temp = n
while temp > 0:
    rem = temp % 10
    print(rem, end = " ")
    temp = temp // 10

print()

#2. reverse of a number
rev = 0
temp = n
while temp > 0:
    rem = temp % 10
    rev = rev * 10 + rem    
    temp = temp // 10
print(rev)

if rev == n:
    print("Palindrome")
else:
    print("Not a palindrome")

