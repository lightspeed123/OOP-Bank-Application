# Custom exception to handle insufficient balance scenarios
class BalanceException(Exception):
    pass

# Class representing a bank account
class BankAccount:
    # Initialize the account with an account name and initial balance
    def __init__(self, account_name, initial_amount):
        self.balance = initial_amount  # Set the initial balance
        self.name = account_name  # Set the account name
        print(f"{self.name}'s account created. ✔️")  # Print confirmation message when account is created
    
    # Method to get the current balance of the account
    def getBalance(self):
        print(f"{self.name}'s Account Balance : 💵{self.balance:.2f}")  # Print balance formatted to 2 decimal places
    
    # Method to deposit an amount into the account
    def deposit(self, amount):
        self.balance = self.balance + amount  # Add the deposit amount to the balance
        print(f"${amount} deposit successful 💰")  # Print success message for deposit
        self.getBalance()  # Display the updated balance
    
    # Method to check if a transaction is viable (i.e., the balance is sufficient)
    def viableTransaction(self, amount):
        if self.balance >= amount:  # Check if the balance is sufficient
            return  # Transaction is viable, do nothing
        else:
            # Raise an exception if the balance is insufficient
            raise BalanceException(f"\nsorry {self.name} has a balance of 💵{self.balance:.2f}")
    
    # Method to withdraw an amount from the account
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)  # Check if the withdrawal is viable
            self.balance = self.balance - amount  # Subtract the amount from balance
            print(f"\n Withdrawn from {self.name}'s account 💴 ")  # Print success message
            self.getBalance()  # Display the updated balance
        except BalanceException as error:
            # Handle the exception if balance is insufficient
            print(f"\n Withdraw Incomplete ❌{error}")  # Print failure message with the error
    
    # Method to transfer an amount to another bank account
    def transfer(self, amount, account):
        try:
            self.viableTransaction(amount)  # Check if the transfer is viable
            self.withdraw(amount)  # Withdraw the amount from the current account
            account.deposit(amount)  # Deposit the amount into the target account
            print(f"Transfer completed from {self.name} account 📦")  # Print success message
        except BalanceException as error:
            # Handle the exception if balance is insufficient
            print(f"Transfer Failed ❌ {error}")  # Print failure message with the error


# Subclass that represents a bank account that earns interest on deposits
class InterestsAcc(BankAccount):
    # Override the deposit method to add interest
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)  # Add deposit with 5% interest
        print("Deposit Completed, Reward earned 💰 ")  # Print success message
        self.getBalance()  # Display the updated balance
