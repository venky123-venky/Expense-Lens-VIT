import json


class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category,
            "amount": self.amount
        }


class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def add_expense(self, name, category, amount):
        expense = Expense(name, category, amount)
        self.expenses.append(expense)
        self.save_expenses()

        print("Expense added successfully!")
        print("Expense saved successfully!")

    def view_expenses(self):
        print("\n---------- EXPENSES ----------")

        if len(self.expenses) == 0:
            print("No expenses added yet.")
            return

        total = 0

        for i, expense in enumerate(self.expenses, start=1):
            print(
                i,
                ".",
                expense.name,
                "|",
                expense.category,
                "| ₹",
                expense.amount
            )

            total += expense.amount

        print("-----------------------------")
        print("Total Expense: ₹", total)

    def analyze_expenses(self):
        print("\n========== EXPENSE ANALYSIS ==========")

        categories = {
            "Food": 0,
            "Travel": 0,
            "Education": 0,
            "Shopping": 0,
            "Entertainment": 0,
            "Other": 0
        }

        for expense in self.expenses:
            categories[expense.category] += expense.amount

        for category, amount in categories.items():
            print(category, ":", "₹", amount)

        total = sum(categories.values())

        print("--------------------------------------")
        print("Total Expense:", "₹", total)

    def delete_expense(self, number):
        if 1 <= number <= len(self.expenses):
            deleted = self.expenses.pop(number - 1)

            self.save_expenses()

            print("Deleted:", deleted.name)
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number!")

    def save_expenses(self):
        data = []

        for expense in self.expenses:
            data.append(expense.to_dict())

        with open("expenses.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Expenses saved successfully!")

    def load_expenses(self):
        try:
            with open("expenses.json", "r") as file:
                data = json.load(file)

            for item in data:
                expense = Expense(
                    item["name"],
                    item["category"],
                    item["amount"]
                )

                self.expenses.append(expense)

        except FileNotFoundError:
            self.expenses = []


print("\n================================")
print("         EXPENSE LENS")
print("================================")

manager = ExpenseManager()


while True:

    print("\n---------- MENU ----------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Analysis")
    print("4. Delete Expense")
    print("5. Save Expenses")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter expense name: ")

        print("\nSelect Category:")
        print("1. Food")
        print("2. Travel")
        print("3. Education")
        print("4. Shopping")
        print("5. Entertainment")
        print("6. Other")

        category_choice = input("Enter category: ")

        if category_choice == "1":
            category = "Food"
        elif category_choice == "2":
            category = "Travel"
        elif category_choice == "3":
            category = "Education"
        elif category_choice == "4":
            category = "Shopping"
        elif category_choice == "5":
            category = "Entertainment"
        elif category_choice == "6":
            category = "Other"
        else:
            print("Invalid category!")
            continue

        try:
            amount = float(input("Enter expense amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than zero!")
                continue

        except ValueError:
            print("Invalid amount! Please enter a number.")
            continue

        manager.add_expense(name, category, amount)

    elif choice == "2":

        manager.view_expenses()

    elif choice == "3":

        manager.analyze_expenses()

    elif choice == "4":

        manager.view_expenses()

        if len(manager.expenses) > 0:
            try:
                number = int(
                    input("Enter expense number to delete: ")
                )

                manager.delete_expense(number)

            except ValueError:
                print("Please enter a valid number!")

    elif choice == "5":

        manager.save_expenses()

    elif choice == "6":

        manager.save_expenses()
        print("\nThank you for using Expense Lens!")
        break

    else:

        print("Invalid choice! Please try again.")