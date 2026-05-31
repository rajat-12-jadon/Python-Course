# Exception Handling in Python

## What is an Exception?

An exception is an unexpected event or error that occurs during program execution and disrupts the normal flow of the program.

---

## Program Crash Without Exception Handling

```python
print("Start")

print(10 / 0)

print("End")
```

### Output

```text
Start
ZeroDivisionError: division by zero
```

The program crashes and `"End"` never executes.

---

## Basic Exception Handling

```python
n = int(input("Enter a number: "))

try:
    print(10 / n)

except ZeroDivisionError:
    print("You can't divide a number by 0")

print("Program continues...")
```

---

## Generic Exception Handling

```python
try:
    print(10 / n)

except Exception as err:
    print(f"An error occurred: {err}")
```

### Why use `Exception as err`?

It stores the error object in `err` so we can print the error message.

---

## else Block

```python
try:
    print(10 / 2)

except Exception as err:
    print(err)

else:
    print("No exception occurred")
```

### Output

```text
5.0
No exception occurred
```

The `else` block runs only when no exception occurs.

---

## finally Block

```python
try:
    print(10 / 0)

except Exception as err:
    print(err)

finally:
    print("I always execute")
```

### Output

```text
division by zero
I always execute
```

The `finally` block always executes.

---

## Raising Custom Exceptions

```python
age = int(input("Enter age: "))

if not (10 <= age <= 18):
    raise ValueError(
        "Age must lie between 10 and 18"
    )
```

### Why use `raise`?

To manually generate exceptions.

---

## Common Exceptions

### ZeroDivisionError

```python
10 / 0
```

### ValueError

```python
int("abc")
```

### TypeError

```python
10 / "5"
```

### IndexError

```python
a = [1, 2]

print(a[10])
```

### KeyError

```python
d = {1: "Hello"}

print(d[5])
```

### NameError

```python
print(x)
```

---

## Flow of try-except-else-finally

```text
try
 |
 |
Exception?
 |
/ \
Yes No
 |   |
except else
   \ /
 finally
    |
 Continue
```

---

## Interview Notes

### try

Contains risky code.

### except

Runs when an exception occurs.

### else

Runs when no exception occurs.

### finally

Always runs.

### raise

Used to manually generate exceptions.
