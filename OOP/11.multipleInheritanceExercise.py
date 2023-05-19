"""
Vehicle Exercise
"""
class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def drive(self):
        print(f'{self.brand} is being driven.')

    def start(self):
        print(f'{self.brand} is starting')

    def stop(self):
        print(f'{self.brand} is stopping.')

class FlyingVehicle:
    def fly(self):
        print(f'{self.brand} is flying.')

class ModernVehicle:
    def status(self):
       print(f'{self.brand} is latest model')

class Car(Vehicle):
    def __init__(self,brand,color):
        super().__init__(brand)
        self.color = color

    def drive(self):
        print(f'{self.brand} with {self.color} is being driven')

class Airplane(Vehicle,FlyingVehicle,ModernVehicle):
    def __init__(self,brand):
        super().__init__(brand)

if __name__ == '__main__':
    airplance = Airplane("Toyota")
    airplance.drive()
    airplance.fly()
    airplance.status()
    airplance.start()
    airplance.stop()





