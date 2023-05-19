"""
Multiple Inheritance
Mult-level Inheritance
"""
class Machine:
    def __init__(self,id):
        self.id = id

    def start(self):
        print("Machine started")

    def stop(self):
        print("Machine stopped")

class Car(Machine):
    def __init__(self,id):
        super().__init__(id)

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def changeGear(self):
        print("Gear Changed")


if __name__ == '__main__':
    car = Car(1)
    car.start()
    car.stop()
    car.changeGear()

