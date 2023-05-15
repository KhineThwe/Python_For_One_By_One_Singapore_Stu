# function arg ---> higher order function
# lazy evaluation
def myFun(x, fn):  # x=5,fn
    return fn(x)  # fn(5)


value = myFun(5, lambda y: y ** 2)
print(value)


# def square(y):
#     return y**2

def myFun1(fn, *args, **kwargs):  # 2,3#kwargs = {y:20}
    return fn(*args, kwargs['y'])  # fn(2,20)
    # return fn(*args, **kwargs)  # fn(2,'y')


# value1 = myFun1(lambda x, y: x ** y, 2, 3)
# print(value1)  # 8
value2 = myFun1(lambda x, y: x + y, 2, y=20)#2+20 = 22
print(value2)

def my_function(**kid):# kid = {fname:"Python",lname = "Class"}---> kid['lname'] = "Python"
    print("Class name is : "+kid['fname']+"  "+kid['lname'])

my_function(fname = "Python",lname = "Class")

