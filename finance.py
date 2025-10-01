class Transaction:
    def __init__(self, amount, category, description=""):
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.category}: {self.amount} ({self.description})"


class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, description=""):
        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)

    def list_transactions(self):
        for i, t in enumerate(self.transactions, start=1):
            print(f"{i}. {t}")

    def total_income(self):
        return sum(t.amount for t in self.transactions if t.amount > 0)

    def total_expenses(self):
        return sum(-t.amount for t in self.transactions if t.amount < 0)

    def balance(self):
        return self.total_income() - self.total_expenses()


# Recursive example: compound interest
def compound_interest(principal, rate, years):
    if years == 0:
        return principal
    return compound_interest(principal * (1 + rate), rate, years - 1)
