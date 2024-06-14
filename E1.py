expenses = []

def add_expense(amount, category):
    expenses.append({'amount': amount, 'category': category})
    print(f'Added expense: ${amount} in category "{category}".')

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("Expense List:")
        for expense in expenses:
            print(f"${expense['amount']} - {expense['category']}")

def view_expenses_by_category(category):
    category_expenses = [expense for expense in expenses if expense['category'] == category]
    if not category_expenses:
        print(f"No expenses found in category: {category}")
    else:
        print(f"Expenses in category '{category}':")
        for expense in category_expenses:
            print(f"${expense['amount']}")

def view_expense_summary():
    if not expenses:
        print("No expenses recorded.")
    else:
        total_expenses = sum(expense['amount'] for expense in expenses)
        print(f"Total Expenses: ${total_expenses}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Expense Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter expense amount ($): "))
            category = input("Enter expense category: ")
            add_expense(amount, category)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category = input("Enter category to view expenses: ")
            view_expenses_by_category(category)
        elif choice == '4':
            view_expense_summary()
        elif choice == '5':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
