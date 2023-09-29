def deposit(account,amount):
    if amount>0:
        account.balance+=amount
        return True
    else:
        return False

def withdraw(account,amount):
    if amount>0 and amount<=account.balance:
        account.balance-=amount
        return True
    else:
        return False