import random
class Bank:
    def __init__(self):
        self.accounts = {}
        self.currentAccountNo = None
        self.name = None
        self.password = None
        self.initialDeposit = None
        print("\t\tWelcome From Python Bank!!!")

    def createAccount(self,name,password,amount):
        accountNumber = random.randint(100, 999)  # 3-digits
        self.accounts[accountNumber] = [name,password,amount]# 0 1 2
        print(f'Account created successfully! your acount number is {accountNumber}')
        self.name = self.accounts[accountNumber][0]
        self.password = self.accounts[accountNumber][1]
        self.initialDeposit = self.accounts[accountNumber][2]
        self.currentAccountNo = accountNumber

    def register(self):
        print("This is from registration")
        userName = input("Please enter your name to register: ")#Camel Case
        userPassword = input("Please enter your password to register: ")
        confirmPassword = input("Enter password again to confirm: ")
        if userPassword == confirmPassword:
            userAmount = int(input("Please enter your amount to register: "))
            self.createAccount(userName,userPassword,userAmount)
            print(self.accounts)
            print("Your current account number : ",self.currentAccountNo)
        else:
            print("Passwords are not equal!!!")
            self.register()

    def login(self):
        pass

    def mainMenu(self):
        while True:
            print("\t\tPress 1 to register")
            print("\t\tPress 2 to Login")
            print("\t\tPress 3 to Quit")
            option = int(input("\t\tPlease chose 1,2,3"))
            if option == 1:
                self.register()
            elif option == 2:
                self.login()
            elif option == 3:
                print("Bye Bye")
                exit(1)
            else:
                print("Invalid option")
                self.mainMenu()




if __name__ == '__main__':
    bank = Bank()#object creation #constructor စအလုပ်လုပ်
    bank.mainMenu()
    # mainMenu()

