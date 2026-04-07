from lib.models import User

users = {}


def get_or_create_user():
    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return None

    if name not in users:
        users[name] = User(name)
        print(f"👤 New user '{name}' created.")

    return users[name]


def add_transaction():
    user = get_or_create_user()
    if user is None:
        return

    title = input("Enter transaction title: ").strip()
    if not title:
        print("Transaction title cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: ").strip())
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    category = input("Enter category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    transaction_type = input("Enter type (income/expense): ").strip().lower()

    try:
        user.add_transaction(title, amount, category, transaction_type)
    except ValueError as error:
        print(f"Error: {error}")


def view_transactions():
    user = get_or_create_user()
    if user is None:
        return

    print(f"\n📋 Transactions for {user.name}")
    user.view_transactions()


def search_transaction():
    user = get_or_create_user()
    if user is None:
        return

    keyword = input("Enter title keyword: ").strip()
    user.search_by_title(keyword)


def filter_category():
    user = get_or_create_user()
    if user is None:
        return

    category = input("Enter category to filter by: ").strip()
    user.filter_by_category(category)


def filter_type():
    user = get_or_create_user()
    if user is None:
        return

    transaction_type = input("Enter type to filter by (income/expense): ").strip().lower()
    user.filter_by_type(transaction_type)


def delete_transaction():
    user = get_or_create_user()
    if user is None:
        return

    try:
        transaction_id = int(input("Enter transaction ID to delete: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a whole number.")
        return

    user.delete_transaction(transaction_id)


def update_transaction_title():
    user = get_or_create_user()
    if user is None:
        return

    try:
        transaction_id = int(input("Enter transaction ID: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a whole number.")
        return

    new_title = input("Enter new title: ").strip()

    try:
        user.update_transaction_title(transaction_id, new_title)
    except ValueError as error:
        print(f"Error: {error}")


def update_transaction_amount():
    user = get_or_create_user()
    if user is None:
        return

    try:
        transaction_id = int(input("Enter transaction ID: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a whole number.")
        return

    try:
        new_amount = float(input("Enter new amount: ").strip())
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    try:
        user.update_transaction_amount(transaction_id, new_amount)
    except ValueError as error:
        print(f"Error: {error}")


def update_transaction_category():
    user = get_or_create_user()
    if user is None:
        return

    try:
        transaction_id = int(input("Enter transaction ID: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a whole number.")
        return

    new_category = input("Enter new category: ").strip()

    try:
        user.update_transaction_category(transaction_id, new_category)
    except ValueError as error:
        print(f"Error: {error}")


def update_transaction_type():
    user = get_or_create_user()
    if user is None:
        return

    try:
        transaction_id = int(input("Enter transaction ID: ").strip())
    except ValueError:
        print("Invalid ID. Please enter a whole number.")
        return

    new_type = input("Enter new type (income/expense): ").strip().lower()

    try:
        user.update_transaction_type(transaction_id, new_type)
    except ValueError as error:
        print(f"Error: {error}")


def show_summary():
    user = get_or_create_user()
    if user is None:
        return

    user.summary()


def show_menu():
    print("\n=== BudgetBuddyCLI ===")
    print("1. Add transaction")
    print("2. View transactions")
    print("3. Search transaction by title")
    print("4. Filter by category")
    print("5. Filter by type")
    print("6. Delete transaction")
    print("7. Update transaction title")
    print("8. Update transaction amount")
    print("9. Update transaction category")
    print("10. Update transaction type")
    print("11. Show summary")
    print("12. Exit")


def main():
    print("💰 Welcome to BudgetBuddyCLI")

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            search_transaction()
        elif choice == "4":
            filter_category()
        elif choice == "5":
            filter_type()
        elif choice == "6":
            delete_transaction()
        elif choice == "7":
            update_transaction_title()
        elif choice == "8":
            update_transaction_amount()
        elif choice == "9":
            update_transaction_category()
        elif choice == "10":
            update_transaction_type()
        elif choice == "11":
            show_summary()
        elif choice == "12":
            print("👋 Exiting BudgetBuddyCLI. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 12.")


if __name__ == "__main__":
    main()