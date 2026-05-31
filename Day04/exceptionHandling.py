# ==========================================================
# Exception Handling in Python
# ==========================================================

# Exception:
# An exception is an unexpected event or error that occurs
# during program execution and disrupts the normal flow
# of the program.


# ==========================================================
# Example 1: Program Crash Without Exception Handling
# ==========================================================

# print("Start")

# print(10 / 0)
# ZeroDivisionError occurs here

# print("End")
# This line never executes because the program crashes


# ==========================================================
# Example 2: Handling ZeroDivisionError
# ==========================================================

n = int(input("Enter a number: "))

try:
    # Risky code
    print(10 / n)

except ZeroDivisionError:
    # Executes only when division by zero occurs
    print("You can't divide a number by 0")

print("Problem solved successfully.")


# ==========================================================
# Example 3: Generic Exception Handling
# ==========================================================

n = int(input("\nEnter another number: "))

try:
    print(10 / n)

except Exception as err:
    # Catches almost all exceptions
    print(f"An error occurred: {err}")

else:
    # Executes only when NO exception occurs
    print("No exception was found.")

finally:
    # Executes whether exception occurs or not
    print("I will always execute.")

print("Execution continues...\n")


# ==========================================================
# Example 4: Handling Type Errors
# ==========================================================

# Uncomment to test

# a = input("Enter a number: ")

# try:
#     print(10 / a)
#
# except Exception as err:
#     print(f"An error occurred: {err}")

# Error:
# TypeError: unsupported operand type(s) for /


# ==========================================================
# Example 5: Raising Custom Exceptions
# ==========================================================

age = int(input("Enter your age: "))

try:

    # Custom validation

    if not (10 <= age <= 18):

        # Manually raise an exception

        raise ValueError(
            "Your age must lie between 10 and 18"
        )

    print("Welcome to the club.")

except Exception as err:

    print(f"An error occurred: {err}")

print("The club will start soon.")


# ==========================================================
# Summary of try-except-else-finally
# ==========================================================

# try
# ----
# Contains code that may produce an exception.


# except
# -------
# Executes when an exception occurs.


# else
# ----
# Executes only when no exception occurs.


# finally
# -------
# Always executes regardless of exception.


# Flow Diagram
#
# try
#   |
#   |
# Exception?
#   |
#  / \
# Yes  No
#  |    |
# except else
#   \   /
#   finally
#      |
#   Continue


# ==========================================================
# Most Common Exceptions
# ==========================================================

# ZeroDivisionError
# -----------------
# 10 / 0


# ValueError
# ----------
# int("abc")


# TypeError
# ---------
# 10 / "5"


# IndexError
# ----------
# a = [1, 2]
# print(a[10])


# KeyError
# --------
# d = {1: "Hello"}
# print(d[5])


# NameError
# ---------
# print(x)
# x is not defined


# ==========================================================
# Interview Definitions
# ==========================================================

# Exception:
# An event that occurs during program execution
# and interrupts the normal flow of the program.


# raise:
# Used to manually generate an exception.


# Exception as err:
# Stores the exception object inside the variable 'err'
# so that the error message can be displayed.