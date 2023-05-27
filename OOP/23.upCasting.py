"""
int()
"""
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof!!")

if __name__ == '__main__':
    dog = Dog()
    dog.sound()

    #upcasting
    animal = dog
    animal.sound()
