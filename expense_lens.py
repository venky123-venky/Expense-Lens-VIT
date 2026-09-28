import json

print("================================")
print("         EXPENSE LENS")
print("================================")

# Load saved expenses
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

# Monthly Budget
while True:
    try:
        budget = float(input("Enter your monthly budget: ₹"))

        if budget <= 0:
            print("Budget must be greater than zero!")
            continue

        break

    except ValueError:
        print("Invalid budget! Please enter a number.")


while True:

    print("\n---------- MENU ----------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Analysis")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ADD EXPENSE
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

        while True:
            try:
                amount = float(input("Enter expense amount: ₹"))

                if amount <= 0:
                    print("Amount must be greater than zero!")
                    continue

                break

            except ValueError:
                print("Invalid amount! Please enter a number.")

        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

        print("Expense added successfully!")
        print("Expense saved successfully!")

    # VIEW EXPENSES
    elif choice == "2":

        print("\n---------- EXPENSES ----------")

        if len(expenses) == 0:
            print("No expenses added yet.")

        else:
            total = 0

            for i, expense in enumerate(expenses, start=1):

                print(
                    i,
                    ".",
                    expense["name"],
                    "|",
                    expense["category"],
                    "| ₹",
                    expense["amount"]
                )

                total += expense["amount"]

            print("-----------------------------")
            print("Total Expense: ₹", total)

            remaining = budget - total

            print("Remaining Budget: ₹", remaining)

            if remaining < 0:
                print("WARNING: You have exceeded your monthly budget!")
            elif remaining <= budget * 0.20:
                print("WARNING: Your remaining budget is low!")
            else:
                print("Budget status: Good")

    # EXPENSE ANALYSIS
    elif choice == "3":

        print("\n========== EXPENSE ANALYSIS ==========")

        categories = {
            "Food": 0,
            "Travel": 0,
            "Education": 0,
            "Shopping": 0,
            "Entertainment": 0,
            "Other": 0
        }

        for expense in expenses:
            categories[expense["category"]] += expense["amount"]

        for category, amount in categories.items():
            print(category, ":", "₹", amount)

        total = sum(categories.values())

        print("--------------------------------------")
        print("Total Expense :", "₹", total)
        print("Remaining     :", "₹", budget - total)

    # DELETE EXPENSE
    elif choice == "4":

        print("\n---------- DELETE EXPENSE ----------")

        if len(expenses) == 0:

            print("No expenses available to delete.")

        else:

            for i, expense in enumerate(expenses, start=1):

                print(
                    i,
                    ".",
                    expense["name"],
                    "|",
                    expense["category"],
                    "| ₹",
                    expense["amount"]
                )

            try:

                delete_number = int(
                    input("Enter expense number to delete: ")
                )

                if 1 <= delete_number <= len(expenses):

                    deleted_expense = expenses.pop(delete_number - 1)

                    with open("expenses.json", "w") as file:
                        json.dump(expenses, file, indent=4)

                    print(
                        "Deleted:",
                        deleted_expense["name"],
                        "| ₹",
                        deleted_expense["amount"]
                    )

                    print("Expense deleted successfully!")

                else:

                    print("Invalid expense number!")

            except ValueError:

                print("Please enter a valid number!")

    # EXIT
    elif choice == "5":

        print("\nThank you for using Expense Lens!")

        break

    else:

        print("Invalid choice! Please try again.")
