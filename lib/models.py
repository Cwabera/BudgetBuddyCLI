class Transaction:
    def __init__(self, transaction_id, title, amount, category, transaction_type):
        if not title or not title.strip():
            raise ValueError("Transaction title cannot be empty.")
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if transaction_type.lower() not in ["income", "expense"]:
            raise ValueError("Transaction type must be 'income' or 'expense'.")
        if not category or not category.strip():
            raise ValueError("Category cannot be empty.")

        self.transaction_id = transaction_id
        self.title = title.strip()
        self.amount = float(amount)
        self.category = category.strip()
        self.transaction_type = transaction_type.lower()

    def update_title(self, new_title):
        if not new_title or not new_title.strip():
            raise ValueError("Transaction title cannot be empty.")
        self.title = new_title.strip()

    def update_amount(self, new_amount):
        if new_amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        self.amount = float(new_amount)

    def update_category(self, new_category):
        if not new_category or not new_category.strip():
            raise ValueError("Category cannot be empty.")
        self.category = new_category.strip()

    def update_type(self, new_type):
        if new_type.lower() not in ["income", "expense"]:
            raise ValueError("Transaction type must be 'income' or 'expense'.")
        self.transaction_type = new_type.lower()

    def __str__(self):
        return (
            f"ID: {self.transaction_id} | "
            f"Title: {self.title} | "
            f"Amount: {self.amount:.2f} | "
            f"Category: {self.category} | "
            f"Type: {self.transaction_type}"
        )


class User:
    def __init__(self, name):
        if not name or not name.strip():
            raise ValueError("User name cannot be empty.")
        self.name = name.strip()
        self.transactions = []
        self.next_id = 1

    def add_transaction(self, title, amount, category, transaction_type):
        transaction = Transaction(self.next_id, title, amount, category, transaction_type)
        self.transactions.append(transaction)
        self.next_id += 1
        print(f"✅ Transaction '{title}' added for {self.name}.")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return

        for transaction in self.transactions:
            print(transaction)

    def get_transaction_by_id(self, transaction_id):
        for transaction in self.transactions:
            if transaction.transaction_id == transaction_id:
                return transaction
        return None

    def delete_transaction(self, transaction_id):
        transaction = self.get_transaction_by_id(transaction_id)
        if transaction:
            self.transactions.remove(transaction)
            print(f"🗑️ Transaction ID {transaction_id} deleted.")
        else:
            print("Transaction not found.")

    def search_by_title(self, keyword):
        results = [t for t in self.transactions if keyword.lower() in t.title.lower()]

        if not results:
            print("No matching transactions found.")
            return

        for transaction in results:
            print(transaction)

    def filter_by_category(self, category):
        results = [t for t in self.transactions if t.category.lower() == category.lower()]

        if not results:
            print("No transactions in that category.")
            return

        for transaction in results:
            print(transaction)

    def filter_by_type(self, transaction_type):
        results = [t for t in self.transactions if t.transaction_type == transaction_type.lower()]

        if not results:
            print("No transactions of that type.")
            return

        for transaction in results:
            print(transaction)

    def total_income(self):
        return sum(t.amount for t in self.transactions if t.transaction_type == "income")

    def total_expenses(self):
        return sum(t.amount for t in self.transactions if t.transaction_type == "expense")

    def balance(self):
        return self.total_income() - self.total_expenses()

    def summary(self):
        summary_data = {
            "total_income": self.total_income(),
            "total_expenses": self.total_expenses(),
            "balance": self.balance(),
            "transaction_count": len(self.transactions),
        }

        print("📊 Budget Summary")
        for key, value in summary_data.items():
            if isinstance(value, float):
                print(f"{key.replace('_', ' ').title()}: {value:.2f}")
            else:
                print(f"{key.replace('_', ' ').title()}: {value}")

    def update_transaction_title(self, transaction_id, new_title):
        transaction = self.get_transaction_by_id(transaction_id)
        if transaction:
            transaction.update_title(new_title)
            print(f"✏️ Transaction ID {transaction_id} title updated.")
        else:
            print("Transaction not found.")

    def update_transaction_amount(self, transaction_id, new_amount):
        transaction = self.get_transaction_by_id(transaction_id)
        if transaction:
            transaction.update_amount(new_amount)
            print(f"✏️ Transaction ID {transaction_id} amount updated.")
        else:
            print("Transaction not found.")

    def update_transaction_category(self, transaction_id, new_category):
        transaction = self.get_transaction_by_id(transaction_id)
        if transaction:
            transaction.update_category(new_category)
            print(f"✏️ Transaction ID {transaction_id} category updated.")
        else:
            print("Transaction not found.")

    def update_transaction_type(self, transaction_id, new_type):
        transaction = self.get_transaction_by_id(transaction_id)
        if transaction:
            transaction.update_type(new_type)
            print(f"✏️ Transaction ID {transaction_id} type updated.")
        else:
            print("Transaction not found.")