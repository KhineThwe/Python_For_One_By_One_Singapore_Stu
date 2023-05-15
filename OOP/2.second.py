class myClass:
    def __init__(self):
        print("Welcome from python course")
        
    def myFun(self):
        print("My function")
#mock
obj1  = myClass()#class ---> constructor
obj1.myFun()

obj2 = myClass()
obj2.myFun()

print(id(obj1))
print(id(obj2))

if id(obj1) == id(obj2):
    print("Addresses are equal")
else:
    print("They are not same")