class Person:
    #special method
    def __init__(self,name,age):#constructor
        print(f'{name} : {age}')

    def welcome(self):
        print(f'Welcome from python course')

if __name__ == '__main__':
    obj = Person("Khine",24)
    #constructor ---> obj ဆောက်လိုက်တာနဲ့တစ်ပြိုင်နက်စတင်အလုပ်လုပ်သည်။
    obj.welcome()
