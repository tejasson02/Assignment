import datetime


class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, amount, category):
        date_today = datetime.date.today()
        key = (date_today.year, date_today.month)

        if key not in self.expenses:
            self.expenses[key] = {}

        if category not in self.expenses[key]:
            self.expenses[key][category] = 0

        self.expenses[key][category] += amount
        print(f"Expense of ${amount} added for category '{category}' on {date_today}.")

    def view_spending_patterns(self):
        for key, value in self.expenses.items():
            year, month = key
            print(f"\nSpending Patterns for {datetime.date(year, month, 1).strftime('%B %Y')}:")
            for category, amount in value.items():
                print(f"{category}: ${amount}")


def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense\n2. View Spending Patterns\n3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            try:
                amount = float(input("Enter the expense amount: $"))
                category = input("Enter the expense category: ")
                expense_tracker.add_expense(amount, category)
            except ValueError:
                print("Invalid input. Please enter a valid number for the expense amount.")
        elif choice == "2":
            expense_tracker.view_spending_patterns()
        elif choice == "3":
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    main()
