# ==========================================================
# File Handling in Python
# ==========================================================

# File Handling:
# File handling is used to store data permanently
# in files instead of storing it temporarily in memory.


# ==========================================================
# Opening a File
# ==========================================================

# Syntax:
#
# file_variable = open("file_name", "mode")

# Example:

# file = open("data.txt", "r")


# ==========================================================
# File Modes
# ==========================================================

# "r"  -> Read Mode
# "w"  -> Write Mode
# "a"  -> Append Mode
# "x"  -> Create New File
# "r+" -> Read + Write
# "w+" -> Write + Read
# "a+" -> Append + Read


# ==========================================================
# Example 1: Reading Entire File
# ==========================================================

file = open("sample.txt", "r")

data = file.read()

print(data)

file.close()


# ==========================================================
# Example 2: Reading First N Characters
# ==========================================================

file = open("sample.txt", "r")

data = file.read(10)

print(data)

file.close()


# ==========================================================
# Example 3: Reading One Line
# ==========================================================

file = open("sample.txt", "r")

line = file.readline()

print(line)

file.close()


# ==========================================================
# Example 4: Reading All Lines
# ==========================================================

file = open("sample.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# ==========================================================
# Example 5: Writing to a File
# ==========================================================

# If file does not exist,
# Python creates it automatically.

file = open("sample.txt", "w")

file.write("Hello Everyone")

file.close()


# ==========================================================
# Example 6: Writing Multiple Lines
# ==========================================================

file = open("sample.txt", "w")

file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3\n")

file.close()


# ==========================================================
# Example 7: Append Mode
# ==========================================================

# Existing content remains unchanged.
# New content is added at the end.

file = open("sample.txt", "a")

file.write("\nNew Line Added")

file.close()


# ==========================================================
# Example 8: Creating a New File
# ==========================================================

# Creates file only if it does not exist.

# file = open("new_file.txt", "x")

# file.close()

# If file already exists:
#
# FileExistsError


# ==========================================================
# Example 9: Using with Statement
# ==========================================================

# Best Practice

with open("sample.txt", "r") as file:

    data = file.read()

    print(data)

# No need to close file manually.
# Python closes it automatically.


# ==========================================================
# Example 10: Writing Using with
# ==========================================================

with open("sample.txt", "w") as file:

    file.write("Hello Python")

# File automatically closes.


# ==========================================================
# Example 11: File Pointer Position
# ==========================================================

with open("sample.txt", "r") as file:

    print(file.tell())

    data = file.read(5)

    print(data)

    print(file.tell())

# tell()
# Returns current cursor position.


# ==========================================================
# Example 12: Moving File Pointer
# ==========================================================

with open("sample.txt", "r") as file:

    file.seek(0)

    print(file.read())

# seek(position)
# Moves cursor to specified position.


# ==========================================================
# Common Exceptions
# ==========================================================

# FileNotFoundError
#
# open("abc.txt", "r")


# PermissionError
#
# Trying to access restricted file


# IsADirectoryError
#
# open("FolderName", "r")


# ==========================================================
# Exception Handling with Files
# ==========================================================

try:

    file = open("sample.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:

    print("File does not exist.")

except Exception as err:

    print(f"Error: {err}")


# ==========================================================
# Reading File Line by Line
# ==========================================================

with open("sample.txt", "r") as file:

    for line in file:

        print(line.strip())

# strip()
# Removes extra newline characters.


# ==========================================================
# Mini Project Example
# ==========================================================

# Write user name into file

name = input("Enter your name: ")

with open("users.txt", "a") as file:

    file.write(name + "\n")

print("Name stored successfully.")


# ==========================================================
# Interview Notes
# ==========================================================

# open()
# ------
# Used to open a file.


# close()
# -------
# Used to close a file.


# read()
# ------
# Reads entire file content.


# readline()
# ----------
# Reads one line at a time.


# readlines()
# -----------
# Reads all lines and returns a list.


# write()
# -------
# Writes content into a file.


# append mode ("a")
# -----------------
# Adds content without removing existing content.


# write mode ("w")
# ----------------
# Overwrites existing content.


# with statement
# --------------
# Automatically closes file.
# Recommended approach.


# tell()
# ------
# Returns current cursor position.


# seek()
# ------
# Moves file cursor to a specified position.