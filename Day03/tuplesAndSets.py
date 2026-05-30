# Tuples are immutable, duplicates, ordered and heterogeneous

# t = (1, 2, 4, 5, 6, 2, 1, 2, print(), True, "Rajat")

# # t[0] = 4 # gives an error as no assignment possible.
# print(t)

# idx = t.index(2) # find the index of a value
# print(idx)
# cnt = t.count(5) # find the frequency of an element in a tuple
# print(cnt)

t = (1) # act as unpacking of elements
print(t)
print(type(t)) # data type is int as act like t = 1

# if you want that single element act as tuple, then write , after element

p = (1,)
print(type(p)) # now data type is tuple

a, b, c, d = (1, 3, 4, 5)
print(type(a)) # datatype is int

# a = 1, 
# b = 3, 
# c = 4, 
# d = 5


# -------------------------------------------------------------------#

#-------------------------Sets---------------------------------------#

# Sets are mutable, non-duplicates, unordered and heterogeneous


s = {1, 2, 9, 3, 12, 3,12, 32, 4, 5, 6, 2, 1, 3, 4}
print(type(s))
print(s)
t = {}

print(type(t)) # empty set act as dictionary
print(hash(32))
# print(s[3]) # gives an error as no indexing allowed 
p = {1, 2, 9, 12, 32}

for item in p:
    print(item, hash(item))

print(hash("Hello"))

print(hash((1, 2, 344)))

# for i in range(len(p)):
#     print(p[i]) # error, no indexing possible as store in hash based

p.add(8)
print(p)

# p.remove(5) # gives an error if element not found
# print(p)

p.discard(5) # no error if element not found
print(p)

popped_element = p.pop()
print(popped_element)
print(p)

p.clear()
print(p)


# Some more functions of Set

# 1. Uninon of Sets

x = {1, 2, 3, 4, 5}
y = {3, 4, 5, 6, 7, 8}

union = x.union(y)
print(union)
print(x | y)

# 2. Intersection of Sets
intersection = x.intersection(y)
print(intersection)
print(x & y)

# 3. Difference of Sets

differenceSet = x.difference(y)
print(differenceSet)
print(y - x)

# 4. Symmetric Difference of Sets

symmetricDifference = x.symmetric_difference(y)
print(symmetricDifference)
print(x ^ y)
