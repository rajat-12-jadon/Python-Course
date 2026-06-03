# ==========================================================
# ENCAPSULATION IN PYTHON
# ==========================================================

# Encapsulation means:
# Bundling data (attributes) and methods together
# inside a class, and restricting direct access
# to some of the object's components.

# Real Life Example:
# ATM Machine -> You can withdraw money, but you
#                cannot access the internal cash vault.
# Capsule      -> Medicine is hidden inside the capsule.


# ==========================================================
# ACCESS MODIFIERS
# ==========================================================

# Python has 3 levels of access:
#
# Public     -> Accessible everywhere
# Protected  -> Accessible within class and subclasses
# Private    -> Accessible only within the class


# ==========================================================
# 1. PUBLIC ATTRIBUTES
# ==========================================================

# No underscore prefix.
# Accessible from anywhere.

class Student:

    def __init__(self, name, age):
        self.name = name    # Public
        self.age = age      # Public


s = Student("Rajat", 22)

print(s.name)   # Accessible
print(s.age)    # Accessible


# ==========================================================
# 2. PROTECTED ATTRIBUTES
# ==========================================================

# Single underscore prefix: _attribute
# Convention: "Do not access outside class/subclass."
# Python does NOT enforce this — it is just a warning.

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self._balance = balance     # Protected

    def show(self):
        print(f"Owner   : {self.owner}")
        print(f"Balance : ₹{self._balance}")


class SavingsAccount(BankAccount):

    def add_interest(self, rate):

        # Subclass can access protected attribute
        self._balance += self._balance * rate / 100
        print(f"New Balance : ₹{self._balance}")


acc = BankAccount("Rajat", 50000)
acc.show()

# Accessible but discouraged outside class
print(acc._balance)

savings = SavingsAccount("Aman", 100000)
savings.add_interest(5)


# ==========================================================
# 3. PRIVATE ATTRIBUTES
# ==========================================================

# Double underscore prefix: __attribute
# Python enforces Name Mangling.
# Cannot be accessed directly from outside the class.

class Employee:

    def __init__(self, name, salary):
        self.name = name            # Public
        self.__salary = salary      # Private

    def show(self):
        print(f"Name   : {self.name}")
        print(f"Salary : ₹{self.__salary}")  # Accessible inside class


emp = Employee("Rajat", 75000)

emp.show()

# Direct access raises AttributeError
# print(emp.__salary)  # AttributeError


# ==========================================================
# NAME MANGLING
# ==========================================================

# Python internally renames __salary to:
# _ClassName__salary

# So it CAN be accessed using the mangled name,
# but this is strongly discouraged.

print(emp._Employee__salary)   # Works but bad practice


# ==========================================================
# 4. GETTERS AND SETTERS
# ==========================================================

# Getters  -> Methods to READ private data
# Setters  -> Methods to UPDATE private data with validation

class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        if len(name) >= 2:
            self.__name = name
        else:
            print("Name must have at least 2 characters.")

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age with validation
    def set_age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("Invalid age.")


p = Person("Rajat", 22)

print(p.get_name())   # Rajat
print(p.get_age())    # 22

p.set_name("Arjun")
p.set_age(25)

print(p.get_name())   # Arjun
print(p.get_age())    # 25

p.set_age(200)        # Invalid age.
p.set_name("R")       # Name too short.


# ==========================================================
# 5. USING @PROPERTY (PYTHONIC GETTERS AND SETTERS)
# ==========================================================

# @property is the Pythonic way to define getters/setters.
# Accessed like attributes, not method calls.

class BankAccount:

    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")

    @property
    def owner(self):
        return self.__owner


acc = BankAccount("Rajat", 50000)

# Accessed like attribute, not method call
print(acc.balance)    # 50000
print(acc.owner)      # Rajat

# Setter called like assignment
acc.balance = 75000
print(acc.balance)    # 75000

acc.balance = -1000   # Balance cannot be negative.


# ==========================================================
# ENCAPSULATION REAL LIFE EXAMPLE
# ==========================================================

class ATM:

    def __init__(self, pin, balance):
        self.__pin = pin            # Private
        self.__balance = balance    # Private

    def withdraw(self, entered_pin, amount):

        if entered_pin != self.__pin:
            print("Wrong PIN. Access Denied.")
            return

        if amount > self.__balance:
            print("Insufficient Balance.")
            return

        self.__balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        print(f"Remaining Balance : ₹{self.__balance}")

    def check_balance(self, entered_pin):

        if entered_pin != self.__pin:
            print("Wrong PIN. Access Denied.")
            return

        print(f"Available Balance : ₹{self.__balance}")


atm = ATM(1234, 100000)

atm.check_balance(1234)
atm.withdraw(1234, 20000)
atm.withdraw(9999, 5000)     # Wrong PIN


# ==========================================================
# SUMMARY
# ==========================================================

# Encapsulation
# -> Bundle data + methods inside a class
# -> Restrict direct access to internal data

# Public (name)
# -> Accessible everywhere

# Protected (_name)
# -> Convention: use only inside class/subclass
# -> Python does not enforce it

# Private (__name)
# -> Name Mangling applied
# -> Not directly accessible outside class

# Getter
# -> Method to read private data

# Setter
# -> Method to update private data with validation

# @property
# -> Pythonic way to define getters/setters


# ==========================================================
# ACCESS MODIFIER QUICK REFERENCE
# ==========================================================

# Modifier    | Syntax      | Access
# ------------|-------------|-----------------------------
# Public      | name        | Anywhere
# Protected   | _name       | Class + Subclass (convention)
# Private     | __name      | Only inside the class