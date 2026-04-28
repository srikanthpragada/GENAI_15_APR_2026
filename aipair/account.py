# Create Account class with id, customer, balance and provide methods like deposit, withdraw and getbalance 
# Validate data and throw exceptions for invalid data

class Account:
    def __init__(self, account_id, customer_name, balance=0):
        self.account_id = account_id
        self.customer_name = customer_name
        self.balance = balance  

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self):
        return self.balance
