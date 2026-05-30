# Deep Copy vs Shallow Copy in Python

## 1. Assignment (Not a Copy)

```python
a = [1, 2, 3]

b = a

b[0] = 10

print(a)
print(b)
```

### Output

```text
[10, 2, 3]
[10, 2, 3]
```

### Explanation

Both variables point to the same list.

```
a ----\
       > [1, 2, 3]
b ----/
```

---

## 2. Shallow Copy

```python
a = [1, 2, 3]

b = a.copy()

b[0] = 10

print(a)
print(b)
```

### Output

```text
[1, 2, 3]
[10, 2, 3]
```

### Explanation

A new outer list is created.

---

## 3. Shallow Copy with Nested Lists

```python
a = [[1, 2], [3, 4]]

b = a.copy()

b[0][0] = 100

print(a)
print(b)
```

### Output

```text
[[100, 2], [3, 4]]
[[100, 2], [3, 4]]
```

### Explanation

The outer list is copied, but inner lists are shared.

```
a ---> [ X , Y ]
          |   |
          v   v
       [1,2] [3,4]

b ---> [ X , Y ]
```

---

## 4. Deep Copy

```python
import copy

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)

b[0][0] = 100

print(a)
print(b)
```

### Output

```text
[[1, 2], [3, 4]]
[[100, 2], [3, 4]]
```

### Explanation

Everything is copied.

```
a ---> [ X , Y ]

b ---> [ P , Q ]
```

No object is shared.

---

## Checking Shared Objects

```python
a = [[1, 2]]

b = a.copy()

print(a is b)
```

Output:

```text
False
```

```python
print(a[0] is b[0])
```

Output:

```text
True
```

---

## Dictionary Example

### Shallow Copy

```python
student = {
    "name": "Rajat",
    "marks": [80, 90]
}

copy_student = student.copy()

copy_student["marks"][0] = 100

print(student)
```

Output:

```text
{'name': 'Rajat', 'marks': [100, 90]}
```

---

### Deep Copy

```python
import copy

student = {
    "name": "Rajat",
    "marks": [80, 90]
}

copy_student = copy.deepcopy(student)

copy_student["marks"][0] = 100

print(student)
```

Output:

```text
{'name': 'Rajat', 'marks': [80, 90]}
```

---

## Interview Summary

| Operation | Outer Object | Inner Objects |
|------------|-------------|--------------|
| `b = a` | Shared | Shared |
| `a.copy()` | New | Shared |
| `copy.copy(a)` | New | Shared |
| `copy.deepcopy(a)` | New | New |

## Golden Rule

For:

```python
[1, 2, 3]
```

`a.copy()` is usually enough.

For:

```python
[[1, 2], [3, 4]]
```

use:

```python
copy.deepcopy()
```

if you want complete independence.