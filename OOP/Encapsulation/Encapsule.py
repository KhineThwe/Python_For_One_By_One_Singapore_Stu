class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number = account_number #protected
        self.__balance = balance #private

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self.__balance

if __name__ == '__main__':
    account = BankAccount("123456",1000)
    #account obj ---> account no ,balance ---> single unit

    #access protected attribute directly
    print(account._account_number)

    #access private attributes using mangled name
    print(account._BankAccount__balance)

    #access attribute using getter method
    print(account.get_account_number())
    print(account.get_balance())

    account.deposit(500)
    print(account.get_balance())

    account.withdraw(200)
    print(account.get_balance())

    account.withdraw(1300)
    print(account.get_balance())

    account.withdraw(1300)
    print(account.get_balance())