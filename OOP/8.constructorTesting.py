class Employee:
    company_name = "ABC"
    def __init__(self):
        print("No argument constructor")

    def __init__(self,name):
        self.name = name
        print(self.name)

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        print(self.name , self.salary)

if __name__ == '__main__':
    emp = Employee("KZT",1000)
