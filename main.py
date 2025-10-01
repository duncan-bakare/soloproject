from finance import FinanceTracker, compound_interest

def menu():
    print("\n--- Personal Finance Tracker ---")
    print("1. Add income")
    print("2. Add expense")
    print("3. View transactions")
    print("4. Show totals")
    print("5. Calculate compound interest")
    print("6. Exit")

def main():
    tracker = FinanceTracker()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            desc = input("Enter description: ")
            tracker.add_transaction(amount, "Income", desc)

        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            desc = input("Enter description: ")
            tracker.add_transaction(-amount, "Expense", desc)

        elif choice == "3":
            tracker.list_transactions()

        elif choice == "4":
            print(f"Total Income: {tracker.total_income()}")
            print(f"Total Expenses: {tracker.total_expenses()}")
            print(f"Balance: {tracker.balance()}")

        elif choice == "5":
            principal = float(input("Enter principal: "))
            rate = float(input("Enter interest rate (e.g., 0.05): "))
            years = int(input("Enter years: "))
            result = compound_interest(principal, rate, years)
            print(f"Future Value: {result:.2f}")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
