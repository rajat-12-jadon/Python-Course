# List is ordered, heterogeneous, mutable, and duplicates

a = [12, 11, 10, 13, 12, True, print()]

# Mutable

a[0] = 1
print(a)


for i in range(len(a)):
    print(a[i])

print(a[0:4:]) #slice of an array

print(a[-1:-4:-1])

b = [1, 2, 3, 4, 5]

for i in range(len(b)): # when need to get access of index
    print(b[i])


for i in b: # directly access values of list
    print(i)

#methods of list

# print(dir(list)) # to see all methods of list

# help(list)  #to see the working of all methods and builtin modules in list

x = [1, 3, 4, 5]

# x.append(6)
# x.append("Rajat")
# x.append(18)

x.insert(1, 2) # insert(index, value)
print(x)
# print(type(x[6]))
# print(type(x[1]))

# Questions Practice

#1. Print all posititve and negative elements of list separately

m = [1, -2, -3, 2, 9, 4, 23, -1, -9]

postNumber = []
negNumber = []
for i in range(len(m)):
    if m[i] < 0:
        negNumber.append(m[i])
    else:
        postNumber.append(m[i])

print(negNumber, postNumber)

# 2. Mean of list element

sum = 0

for i in range(len(m)):
    sum += m[i]

print(sum / len(m))

# 3. print greatest element with its index

idx = 0
greatVal = m[0]

for i in range(len(m)):
    if m[i] > greatVal:
        greatVal = m[i]
        idx = i

print(greatVal, idx)


# 4. Find second largest element
greatVal = m[0]
secondGreater = float('-inf')

for num in m:
    if num > greatVal:
        secondGreater = greatVal
        greatVal = num

    elif num > secondGreater and num != greatVal:
        secondGreater = num

print("Largest:", greatVal)
print("Second Largest:", secondGreater)


# 5. check if list is sorted or not

num = [1, 2, 4, 5, 6]

for i in range(len(num) - 1):
    if num[i] > num[i+1]:
        print(False)
        break
else:
    print(True)
