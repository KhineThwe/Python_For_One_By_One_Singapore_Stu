import zope.interface
"""In interface class ---> all methods of an interface are abstract---> slow
--> pip install zope.interface
"""
class MyInterface(zope.interface.Interface):
    # x = zope.interface.Attribute("python")
    def method1(self):
        pass
    def method2(self):
        pass
    # def normal(self):
    #     print("Hi Normal Method")

@zope.interface.implementer(MyInterface)
class derivedClass:
    def method1(self):
        print("Hello:")
    def method2(self):
        print("Hello from method 2")

if __name__ == '__main__':
    # print(type(MyInterface))
    # print(MyInterface.__module__)
    # print(MyInterface.__name__)
    # x = MyInterface['x']
    # print(x)
    # print(type(x))

    der = derivedClass()
    der.method1()
    der.method2()
    # der.normal()

