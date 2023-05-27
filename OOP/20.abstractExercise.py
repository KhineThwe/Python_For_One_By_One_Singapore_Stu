from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

"""implements"""
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

if __name__ == '__main__':
    rectangle = Rectangle(5,3)
    circle = Circle(2)

    print(rectangle.area())
    print(circle.area())
