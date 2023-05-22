"""
private ---> __varname or __methodName --> __
protected ---> _varname
"""
class Parent:
    def __init__(self,age):
        self.it   = age

    def getData(self):
        print(self._age)

class Sub(Parent):
    def getData(self):
        print(self._age)

if __name__ == '__main__':
    # sub = Sub(21)
    # sub.getData()

    # parent = Parent(21)
    # parent.getData()