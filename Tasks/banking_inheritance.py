class AccountOpening:

    def getdata(self):
        self.name = input("Enter the name of the account holder: ")
        self.account_number = input("Enter the account number: ")
        self.account_type = input("Enter the Account Type: ")
        self.balance = 0  


class Deposit(AccountOpening):

    def deposit(self):
        amount = int(input("Enter the amount to deposit: "))
        if amount < 2000:
            print("Minimum deposit amount is 2000.")
        else:
            self.balance += amount
            print("Amount deposited successfully.")


class Withdraw(Deposit):

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")


class Statement(Withdraw):

    def printdata(self):
        print("\n Account Statement")
        print("Account Holder Name:", self.name)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)
        print("Account Type:", self.account_type)


s1 = Statement()
s1.getdata()
s1.deposit()
s1.withdraw()
s1.printdata()

print("Thank you for banking with us!")