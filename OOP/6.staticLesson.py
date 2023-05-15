class Calculator:
    @staticmethod
    def addNumbers(x,y):
        return x+y

if __name__ == '__main__':
    # cal = Calculator()
    # print(cal.addNumbers(10,20))
    print(Calculator.addNumbers(10,20))