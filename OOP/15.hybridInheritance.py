class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f'{self.brand} is starting')

    def stop(self):
        print(f'{self.brand} is stopping')

class FlyingVehicle(Vehicle):
    def fly(self):
        print(f'{self.brand} is flying')

class LandVehicle(Vehicle):
    def drive(self):
        print(f'{self.brand} is driving')

class AmphibiousVehicle(FlyingVehicle,LandVehicle):
    def __init__(self,brand):
        super().__init__(brand)

if __name__ == '__main__':
    amphibious_vehicle = AmphibiousVehicle("AmphibiousOne")
    amphibious_vehicle.start()
    amphibious_vehicle.fly()
    amphibious_vehicle.drive()
    amphibious_vehicle.stop()