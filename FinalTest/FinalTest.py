class BankingError(Exception):
    pass

class InvalidAmountError(BankingError):
    pass

class InsufficientBalanceError(BankingError):
    pass

class MinimumBalanceError(BankingError):
    pass

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance.")
        self.balance -= amount

    def display_details(self):
        print(f"Account No: {self.account_number}")
        print(f"Holder Name: {self.account_holder}")
        print(f"Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, minimum_balance):
        super().__init__(account_number, account_holder, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount < 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise MinimumBalanceError("Cannot withdraw: Minimum balance limit reached.")
        self.balance -= amount

accounts = []

try:
    acc1 = BankAccount(101, "Mahe", 5000)
    acc2 = SavingsAccount(102, "Shubham", 8000, 2000)
    acc3 = SavingsAccount(103, "Arun", 10000, 3000)

    acc1.deposit(2000)
    acc2.withdraw(3000)
    acc3.withdraw(5000)

    accounts.extend([acc1, acc2, acc3])

except BankingError as e:
    print("Banking Error:", e)

print("\nAll Account Details:")
for acc in accounts:
    acc.display_details()

 