class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        self.history.append(f"Deposited Rs {amount}")
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.history.append(f"Withdrawn Rs {amount}")
    def show_history(self):
        for transaction in self.history:
            print(transaction)
account = BankAccount("Ali", 1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.balance)
account.show_history()