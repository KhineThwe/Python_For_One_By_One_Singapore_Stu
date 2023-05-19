class Account:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f'Deposited {amount} into Account {self.account_number}.'
              f'Current balance {self.balance}')

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'Withdraw {amount} from Account {self.account_number}'
                  f'Current balance {self.balance}')

class InterestBearingAccount:
    def __init__(self,interest_rate):
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f'Calculated interest: {interest}')

class CheckingAccount(Account):
    def __init__(self,account_number,balance):
        super().__init__(account_number,balance)

    def process_check(self,check_amount):
        self.withdraw(check_amount)
        print(f'Processed check for Account {self.account_number} with'
              f'amount: {check_amount}')
#Loan
class SavingsAccount(Account,InterestBearingAccount):
    def __init__(self,account_number,balance,interest_rate):
        Account.__init__(self,account_number,balance)
        InterestBearingAccount.__init__(self,interest_rate)

    def add_interest(self):
        self.calculate_interest()
        self.deposit(self.balance * self.interest_rate)

if __name__ == '__main__':
    checking_acount = CheckingAccount("ACC001",1000)
    saving_account = SavingsAccount("SVACC001",5000,0.05)

    checking_acount.deposit(200)
    checking_acount.process_check(500)

    saving_account.deposit(1000)
    saving_account.add_interest()
