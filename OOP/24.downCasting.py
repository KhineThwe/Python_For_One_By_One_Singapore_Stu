class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof!!")

    def wag_tail(self):
        print("Tail Wagging")

if __name__ == '__main__':
    animal = Animal()
    animal.sound() #Animal Sound

    dog = Dog()
    dog.sound()
    dog.wag_tail()

    dog_animal  = Animal()
    dog_animal.sound()
    # dog_animal.wag_tail()

    dog_animal1 = Dog()
    dog_animal1.sound()
    dog_animal1.wag_tail()

    dog = dog_animal#Downcasting
    dog.sound()

    animal = dog_animal1#Upcasting
    animal.sound()
    animal.wag_tail()




