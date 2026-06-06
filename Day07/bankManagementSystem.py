# ==========================================================
# BANK MANAGEMENT SYSTEM
# ==========================================================
#
# Features:
# - Create Account
# - Deposit Money
# - Withdraw Money
# - View Details
# - Update Details
# - Delete Account
#
# Concepts Used:
# - OOP
# - JSON
# - File Handling
# - Class Methods
# - Encapsulation
# - List Comprehensions
#
# Data Storage:
# - data.json
#
# Author: Rajat Jadon
#
# ==========================================================

import json
import random
import string
from pathlib import Path


class Bank:
    """
    Bank Management System

    Features:
    - Create Account
    - Deposit Money
    - Withdraw Money
    - View User Details
    - Update User Details
    - Delete Account

    Data is stored in data.json
    """

    # Path of JSON file used as database
    database = Path(__file__).parent / "data.json"

    # Stores all user records loaded from JSON
    data = []

    try:

        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists.")

    except Exception as err:
        print(f"An error occurred as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __generateAccountNumber(cls):
        return random.randint(100000000000, 999999999999)

    def createAccount(self):
        userInfo = {
            "Name": input("Tell your name: "),
            "Age": int(input("Enter your age: ")),
            "E-Mail": input("Enter your email: "),
            "PIN": int(input("Tell your four digit pin: ")),
            "Account Number": Bank.__generateAccountNumber(),  # FIXED: was Bank._Bank__generateAccountNumber()
            "Balance": 0
        }

        if userInfo['Age'] < 18 or len(str(userInfo['PIN'])) != 4:
            print("Sorry, you can't create your account.")
        else:
            print("Thank you, your account has been created successfully.")

            for i in userInfo:
                print(f"{i} : {userInfo[i]}")

            print("Please note your account number for future reference.")

            Bank.data.append(userInfo)

            Bank.__update()  # FIXED: was Bank._Bank__update()

    def depositMoney(self):
        accNumber = int(input("Please enter your account number: "))
        pinNumber = int(input("Please enter your PIN: "))

        userData = [
            i for i in Bank.data
            if i['Account Number'] == accNumber and i['PIN'] == pinNumber
        ]

        if len(userData) == 0:
            print("Sorry, no data found!!")
        else:
            amount = int(input("How much money you want to deposit: "))

            if amount > 10000 or amount < 0:
                print("Sorry, the amount limit is only less than 10000 and above 0")
            else:
                userData[0]['Balance'] += amount
                Bank.__update()  # FIXED: was Bank._Bank__update()
                print("Amount deposited successfully.")

    def withdrawMoney(self):
        accNumber = int(input("Please enter your account number: "))
        pinNumber = int(input("Please enter your PIN: "))

        userData = [
            i for i in Bank.data
            if i['Account Number'] == accNumber and i['PIN'] == pinNumber
        ]

        if len(userData) == 0:
            print("Sorry, no data found!!")
        else:
            amount = int(input("How much money you want to withdraw: "))

            if amount > userData[0]['Balance']:
                print("Sorry, insufficient balance")
            else:
                userData[0]['Balance'] -= amount
                Bank.__update()  # FIXED: was Bank._Bank__update()
                print("Amount withdrawal successfully.")

    def userDetails(self):
        accNumber = int(input("Please enter your account number: "))
        pinNumber = int(input("Please enter your PIN: "))
        
        userData = [i for i in Bank.data if i['Account Number'] == accNumber and i['PIN'] == pinNumber]

        if len(userData) == 0:
            print("Sorry, no data found!!")
            return

        print("Your details: \n")

        for i in userData[0]:
            print(f"{i} : {userData[0][i]}")

        print()

    def updateDetails(self):
        accNumber = int(input("Please enter your account number: "))
        pinNumber = int(input("Please enter your PIN: "))
        
        userData = [i for i in Bank.data if i['Account Number'] == accNumber and i['PIN'] == pinNumber]

        if len(userData) == 0:
            print("No such user found.")
        else:
            print("You can change your name, your PIN and your Email ID only. ")

            print("Fill out the detals for change or leave it empty if no changes required: ")
            newData = {
                "Name" : input("Enter new name you want to update or leave if no need to update: "),
                "E-Mail" : input("Enter new email if you want to update or leave it: "),
                "PIN" : input("Enter your new PIN: ")
            }

            if newData["Name"] == "":
                newData["Name"] = userData[0]['Name']
            if newData["E-Mail"] == "":
                newData["E-Mail"] = userData[0]['E-Mail']
            if newData["PIN"] == "":
                newData["PIN"] = userData[0]["PIN"]
            else:
                newData["PIN"] = int(newData["PIN"])

            newData['Age'] = userData[0]['Age']
            newData['Account Number'] = userData[0]['Account Number']
            newData['Balance'] = userData[0]['Balance']

            for i in newData:
                if newData[i] == userData[0][i]:
                    continue
                else:
                    userData[0][i] = newData[i]

            Bank.__update()  # FIXED: was Bank._Bank__update()
            print("Details are updated successfully.")
            print()
            
    def deleteUser(self):
        accNumber = int(input("Please enter your account number: "))
        pinNumber = int(input("Please enter your PIN: "))

        userData = [
            i for i in Bank.data
            if i['Account Number'] == accNumber and i['PIN'] == pinNumber
        ]

        if len(userData) == 0:
            print("No such user found.")
        else:
            check = input("Press 'Y' if you want to delete your account or press 'N': ")

            if check == 'n' or check == 'N':
                print("By passed.")
            else:
                index = Bank.data.index(userData[0])
                Bank.data.pop(index)
                print("Account deleted successfully.")
                Bank.__update()  # FIXED: was Bank._Bank__update()


# ----------------------------------------------------------
# MAIN LOOP — Added loop + exit option (everything else same)
# ----------------------------------------------------------

user = Bank()

while True:  # ADDED: loop so user can perform multiple operations
    print("\nPress 1 for creating an account.")
    print("Press 2 for depositing the money in your account.")
    print("Press 3 for withdrawing the money from your account.")
    print("Press 4 for getting your details.")
    print("Press 5 for updating you details.")
    print("Press 6 for deleting your account.")
    print("Press 7 to Exit.")  # ADDED: exit option

    check = int(input("Tell your response: "))

    if check == 1:
        user.createAccount()

    elif check == 2:
        user.depositMoney()

    elif check == 3:
        user.withdrawMoney()

    elif check == 4:
        user.userDetails()

    elif check == 5:
        user.updateDetails()

    elif check == 6:
        user.deleteUser()

    elif check == 7:  # ADDED: exit condition
        print("Thank you for using the Bank Management System. Goodbye!")
        break