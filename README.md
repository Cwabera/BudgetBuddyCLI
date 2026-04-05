# 💰 BudgetBuddy CLI

## 📌 Description

**BudgetBuddy CLI** is a Python command-line application that allows users to track and manage their personal finances directly from the terminal. Users can add, view, update, delete, and analyze their income and expenses in an interactive and user-friendly way.

The application is built using **Object-Oriented Programming (OOP)** principles and provides a structured approach to managing financial transactions.

---

## 🧠 Features

* Add new transactions (income or expense)
* View all transactions
* Search transactions by title
* Filter transactions by category
* Filter transactions by type (income/expense)
* Update transaction details (title, amount, category, type)
* Delete transactions
* View financial summary (income, expenses, balance)

---

## 🔁 CRUD Operations

This project includes more than 8 CRUD operations:

### ✅ Create

* Add a new transaction

### 📖 Read

* View all transactions
* Search by title
* Filter by category
* Filter by type
* View summary

### ✏️ Update

* Update transaction title
* Update transaction amount
* Update transaction category
* Update transaction type

### 🗑️ Delete

* Delete a transaction

---

## 🧩 Object Relationship

**User → Transactions (1 : Many)**

* One `User` can have multiple `Transaction` objects
* Each transaction belongs to one user

---

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Lists and Dictionaries
* Command-Line Interface (CLI)

---

## 📁 Project Structure

```
lib/
    __init__.py
    models.py
    cli_tool.py

testing/
    __init__.py
    test_cli_tool.py
```

---

## ▶️ How to Run the Application

From the root project folder, run:

```bash
python3 -m lib.cli_tool
```

---

## 💻 Example Usage

```
=== BudgetBuddyCLI ===
1. Add transaction
2. View transactions
3. Search transaction by title
4. Filter by category
5. Filter by type
6. Delete transaction
7. Update transaction title
8. Update transaction amount
9. Update transaction category
10. Update transaction type
11. Show summary
12. Exit
```

---

## 🧪 Running Tests

To run the tests:

```bash
pytest
```

Or:

```bash
pytest testing/test_cli_tool.py
```

---

## ⚠️ Important Notes

* All data is stored **in memory only**
* Once the program exits, all transactions are lost
* This is intentional for simplicity unless persistence is required

---

## 🚀 Future Improvements

* Add file storage (JSON or database)
* Add user authentication
* Add multiple users with persistent data
* Improve UI/UX of CLI output

---

## 👤 Author

Charles Ngatia
