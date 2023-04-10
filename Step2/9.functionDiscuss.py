def greet():#no parmeter fun
    print(f'Hello')

def greet_name(n):#parameterized fun#n = "Khine"
    print("Welcome",n)

def greet_name_and_age(n,a):#2
    print(f'{n} : {a}')

#default value or parameter
def name_return(name="Khine"):
    print(f'Hello {name}')

if __name__ == '__main__':
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    greet()
    greet_name(name)#greet_name("Khine")
    greet_name_and_age(name,age)
    name_return(name)