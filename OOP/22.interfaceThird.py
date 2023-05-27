from zope.interface import Interface,implementer,Attribute

class IShape(Interface):
    def area(self):
        pass

    perimeter = Attribute("The perimeter of the shape.")

@implementer(IShape)
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width+ self.height)

if __name__ == '__main__':
    rectangle = Rectangle(5,3)
    print(rectangle.area())
    print(rectangle.perimeter)

