# 🏦 Bank Management System

A command-line banking application built in Python that lets users create and manage bank accounts with full CRUD operations. Account data is persisted locally using a JSON file as a lightweight database.

---

## Features

- **Create Account** — Register a new bank account with name, age, email, and PIN
- **Deposit Money** — Add funds to your account (up to ₹10,000 per transaction)
- **Withdraw Money** — Withdraw funds with balance validation
- **View Details** — Display all account information securely
- **Update Details** — Change your name, email, or PIN
- **Delete Account** — Permanently remove your account with confirmation

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- No third-party libraries required (uses only the standard library)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/bank-management-system.git

# Navigate into the project folder
cd bank-management-system
```

### Run

```bash
python bank_management.py
```

---

## Usage

On running the script, a menu is displayed:

```
Press 1 for creating an account.
Press 2 for depositing the money in your account.
Press 3 for withdrawing the money from your account.
Press 4 for getting your details.
Press 5 for updating your details.
Press 6 for deleting your account.
Press 7 to Exit.
```

Enter the number for the operation you want to perform. The menu loops until you press `7` to exit.

---

## Project Structure

```
bank-management-system/
│
├── bank_management.py   # Main application file
├── data.json            # Auto-generated database file (created on first run)
└── README.md            # Project documentation
```

> `data.json` is created automatically when the first account is added. You can add it to `.gitignore` if you don't want to push user data to GitHub.

---

## Concepts Used

| Concept | Where Used |
|---|---|
| OOP (Classes & Objects) | `Bank` class encapsulates all banking logic |
| Encapsulation | Private methods `__update`, `__generateAccountNumber` |
| File Handling | Reading and writing `data.json` |
| JSON | Storing and loading account records |
| List Comprehensions | Filtering user records by account number and PIN |
| Class Methods | `__update` and `__generateAccountNumber` use `@classmethod` |

---

## Constraints & Validations

- Minimum age to open an account: **18 years**
- PIN must be exactly **4 digits**
- Maximum deposit per transaction: **₹10,000**
- Withdrawals cannot exceed the **available balance**

---

## Data Storage

All account data is stored in `data.json` in the following format:

```json
[
    {
        "Name": "Rajat Jadon",
        "Age": 21,
        "E-Mail": "rajat@example.com",
        "PIN": 1234,
        "Account Number": 482910374651,
        "Balance": 5000
    }
]
```

---

## Author

**Rajat Jadon**
    