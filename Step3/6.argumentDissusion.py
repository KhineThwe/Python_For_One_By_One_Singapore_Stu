"""
1.Default argument
2.Keyword argument(named arguments)
3.Positional argument
4.Arbitrary arguments(*args and **kwargs)
**kwargs ---> arbitrary keyword argument
"""
def student(name,age,grade="A",school="Harvard"):
    """default argument testing"""
    print("Student Details: ",name,age,grade,school)

student('John',24,'E','MIT')
print(student.__doc__)

def student1(name,age):
    """keyword argument testing"""
    print("Student Details: ",name,age)

student1(name="Kelvin",age=24)

"""positional arg"""
def subtract(a,b):
    print(a-b)
subtract(7,8)#positional arg
subtract(b=7,a=8)#as a keyword arg

"""*args"""
def percentage(*args):
    sum = 0 #global var
    for i in args:
        sum+=i
    avg = sum/len(args)
    print("Average",avg)

percentage(33,44,55)

"""Arbitrary keyword argument (**kwargs)
Keyword argument passed to kwargs are accessed using key-value pair like dictionary 
"""

def percentage1(**kwargs):
    sum = 0
    for i in kwargs:
        sub_name = i
        sub_marks = kwargs[i]
        print(sub_name,"=",sub_marks)

percentage1(math=56,english=61,science=73)#keyword argument