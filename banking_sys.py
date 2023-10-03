from Bank.account import SavingsAccount,CheckingAccount
from Bank.transaction import deposit,withdraw

savings_account=SavingsAccount("NIBIL","Anusha",1000,2.5)
checking_account=CheckingAccount("CA678","Bipana",10000,5.1)

savings_account.display_info()
checking_account.display_info()

deposit(savings_account,600)
withdraw(checking_account,500)

print("\nUpdated information: ")
savings_account.display_info()
checking_account.display_info()

interest=savings_account.calc_interest()
print(f"Interest earned: Rs{interest:.2f}")