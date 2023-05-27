#abstract
from abc import ABC,abstractmethod
"""
without body only header ---> abstract method --> fast
"""
#abstract class
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    def normal(self):
        print("Hi Normal method")

"""implements"""
class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    dog.speak()
    cat.speak()
    dog.normal()
