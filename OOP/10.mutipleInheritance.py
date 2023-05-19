"""
Multiple Inheritance
-derived class can inherit from more than one parent

Syntax:
class DerivedClass(BaseClass1,BaseClass2,.......)
     #class body
"""
class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

class Flyable:
    def fly(self):
        print(f'{self.name} is flying')

class Bird(Animal,Flyable):
    def __init__(self,name):
        super().__init__(name)

if __name__ == '__main__':
    bird = Bird("Sparrow")
    bird.eat()
    bird.fly()

