class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

class Mammal(Animal):
    def __init__(self,name):
        super().__init__(name)

    def give_birth(self):
        print(f'{self.name} is giving birth')

class Reptile(Mammal):
    def __init__(self,name):
        super().__init__(name)

    def lay_eggs(self):
        print(f'{self.name} is laying eggs')

class Dog(Mammal):
    def __init__(self,name):
        super().__init__(name)

    def bark(self):
        print(f'{self.name} is barking')

class Snake(Reptile):
    def __init__(self,name):
        super().__init__(name)

    def hiss(self):
        print(f'{self.name} is hissing')

if __name__ == '__main__':
    dog = Dog("Teddy")
    dog.eat()
    dog.sleep()
    dog.bark()
    dog.give_birth()

    snake = Snake("Cobra")
    snake.eat()
    snake.sleep()
    snake.lay_eggs()
    snake.hiss()


"""
Shape ---> draw

circle 
rectangle
"""