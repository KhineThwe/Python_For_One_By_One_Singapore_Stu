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
        self.beautifyPrint(f'Account created successfully! your acount number is {accountNumber}')
        self.name = self.accounts[accountNumber][0]
        self.password = self.accounts[accountNumber][1]
        self.initialDeposit = self.accounts[accountNumber][2]
        self.currentAccountNo = accountNumber

    def beautifyPrint(self,message):
        print("--------------------------------------")
        print(message)
        print("--------------------------------------")

    def allInfo(self):
        for x,y in self.accounts.items():
            print("----------------------")
            print("Account No: ",x)
            print("Username : ",y[0])
            print("Password: ",y[1])
            print("Amount: ",y[2])
            print("----------------------")

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
            self.allInfo()
        else:
            print("Passwords are not equal!!!")
            self.register()

    def authenticate(self,uname,accountNo):
        if accountNo in self.accounts.keys() and uname == self.accounts[accountNo][0]:
            return True
        else:
            return False

    def login(self):
        print("This is from login")
        loginAccountNo = int(input("Enter account no to login: "))#564
        loginName = input("Enter username to login: ")
        if self.authenticate(loginName,loginAccountNo):
            self.beautifyPrint("Account authenticated!Login Successful!")
            self.exchange()
        else:
            self.beautifyPrint("Login Fail!!!Try again!")
            self.mainMenu()


    def exchange(self):
        print("This is from exchange!")
      
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

