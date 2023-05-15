class myClass:
    def __init__(self,value1,value2):
        self.x = value1
        self.y = value2

    def myMethod(self):
        print(self.x,self.y)

if __name__ == '__main__':
    obj1 = myClass(10,20)
    obj1.myMethod()


    obj2 = myClass(20,40)
    obj2.myMethod()
