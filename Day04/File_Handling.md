# File Handling in Python

## What is File Handling?

File handling is used to store data permanently in files.

Without files, data is lost when the program terminates.

---

# Opening a File

```python
file = open("sample.txt", "r")
```

### Syntax

```python
open(filename, mode)
```

---

# File Modes

| Mode | Description       |
| ---- | ----------------- |
| r    | Read              |
| w    | Write (overwrite) |
| a    | Append            |
| x    | Create file       |
| r+   | Read + Write      |
| w+   | Write + Read      |
| a+   | Append + Read     |

---

# Reading Entire File

```python
file = open("sample.txt", "r")

data = file.read()

print(data)

file.close()
```

---

# Reading First N Characters

```python
file = open("sample.txt", "r")

print(file.read(10))

file.close()
```

---

# Reading One Line

```python
file = open("sample.txt", "r")

print(file.readline())

file.close()
```

---

# Reading All Lines

```python
file = open("sample.txt", "r")

print(file.readlines())

file.close()
```

---

# Writing to a File

```python
file = open("sample.txt", "w")

file.write("Hello Python")

file.close()
```

### Important

Write mode removes old content before writing.

---

# Writing Multiple Lines

```python
file = open("sample.txt", "w")

file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3\n")

file.close()
```

---

# Append Mode

```python
file = open("sample.txt", "a")

file.write("\nNew Line")

file.close()
```

Append mode keeps existing content and adds new content at the end.

---

# Creating a New File

```python
file = open("new_file.txt", "x")

file.close()
```

### Error

```text
FileExistsError
```

if the file already exists.

---

# Best Practice: with Statement

```python
with open("sample.txt", "r") as file:

    data = file.read()

    print(data)
```

### Advantage

No need to call:

```python
file.close()
```

Python closes the file automatically.

---

# tell()

Returns current cursor position.

```python
with open("sample.txt", "r") as file:

    print(file.tell())

    file.read(5)

    print(file.tell())
```

---

# seek()

Moves file cursor.

```python
with open("sample.txt", "r") as file:

    file.seek(0)

    print(file.read())
```

---

# Reading Line by Line

```python
with open("sample.txt", "r") as file:

    for line in file:

        print(line.strip())
```

### strip()

Removes newline characters.

---

# File Exceptions

## FileNotFoundError

```python
open("abc.txt", "r")
```

## PermissionError

Trying to access a restricted file.

## IsADirectoryError

```python
open("FolderName", "r")
```

---

# File Handling with Exception Handling

```python
try:

    with open("sample.txt", "r") as file:

        print(file.read())

except FileNotFoundError:

    print("File not found")

except Exception as err:

    print(err)
```

---

# Mini Project Example

```python
name = input("Enter your name: ")

with open("users.txt", "a") as file:

    file.write(name + "\n")

print("Saved Successfully")
```

---

# Interview Notes

### open()

Opens a file.

### close()

Closes a file.

### read()

Reads entire file.

### readline()

Reads one line.

### readlines()

Reads all lines into a list.

### write()

Writes data into file.

### tell()

Returns cursor position.

### seek()

Moves cursor.

### with

Recommended way to work with files.
