from lib.models import User, Transaction


def test_add_transaction():
    user = User("Alice")
    user.add_transaction("Salary", 50000, "Income", "income")

    assert len(user.transactions) == 1
    assert user.transactions[0].title == "Salary"
    assert user.transactions[0].amount == 50000.0


def test_get_transaction_by_id():
    user = User("Alice")
    user.add_transaction("Rent", 12000, "Housing", "expense")

    transaction = user.get_transaction_by_id(1)

    assert transaction is not None
    assert transaction.title == "Rent"


def test_delete_transaction():
    user = User("Alice")
    user.add_transaction("Lunch", 500, "Food", "expense")
    user.delete_transaction(1)

    assert len(user.transactions) == 0


def test_update_transaction_title():
    user = User("Alice")
    user.add_transaction("Lunch", 500, "Food", "expense")
    user.update_transaction_title(1, "Dinner")

    assert user.transactions[0].title == "Dinner"


def test_update_transaction_amount():
    user = User("Alice")
    user.add_transaction("Lunch", 500, "Food", "expense")
    user.update_transaction_amount(1, 800)

    assert user.transactions[0].amount == 800.0


def test_update_transaction_category():
    user = User("Alice")
    user.add_transaction("Lunch", 500, "Food", "expense")
    user.update_transaction_category(1, "Dining")

    assert user.transactions[0].category == "Dining"


def test_update_transaction_type():
    user = User("Alice")
    user.add_transaction("Bonus", 2000, "Work", "income")
    user.update_transaction_type(1, "expense")

    assert user.transactions[0].transaction_type == "expense"


def test_total_income_and_expenses():
    user = User("Alice")
    user.add_transaction("Salary", 50000, "Income", "income")
    user.add_transaction("Groceries", 2000, "Food", "expense")
    user.add_transaction("Transport", 1000, "Travel", "expense")

    assert user.total_income() == 50000.0
    assert user.total_expenses() == 3000.0
    assert user.balance() == 47000.0