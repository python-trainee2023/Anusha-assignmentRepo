class Account:
    def __init__(self,account_number,holder_name,balance):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=balance

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"balance: {self.balance:.2f}")

class SavingsAccount(Account):
    def __int__(self,account_number,holder_name,balance,interest_rate):
        Account.__init__(account_number,holder_name,balance)
        self.interest_rate=interest_rate
        self.balance=balance

    def calc_interest(self):
        return self.balance*(self.interest_rate/100)

class CheckingAccount(Account):
    def __init__(self,account_number,holder_name,balance,overdraft_limit):
        super().__init__(account_number,holder_name,balance)
        self.overdraft_limit=overdraft_limit

    def withdraw(self,amount):
        if amount<=self.balance+self.overdraft_limit:
            self.balance-=amount
            return True
            print("withdrawal was successful")
        else:
            return False
            print("withdrawal was not successful")
