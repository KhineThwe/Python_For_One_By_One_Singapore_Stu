#docstring က function ရဲ့ body
#function ထဲရှိ arg ----> function annotation
#PEP python enhancement proposal
#def myFun(a:<expression>,b:<expression>)->'return of function'
def myFun(a:'annotation of a',b:'annotation of b')->'return of function':
    """this is body expression for myfun"""
    return a*b
print(myFun.__doc__)
print(myFun.__annotations__)

#another function
x = 3
y = 5
def myFun1(a:'some value from funCall')->'multiply'+str(max(x,y))+'times':
    """This function will return multiply of max"""
    return a*max(x,y)

data = myFun1(2)
print(data)
print(myFun1.__annotations__)

def myFun2(a:'some value from funCall',b:'some value from funCall')->'b'+'a'+'multiply'+str(max(x,y))+'times':
    """This function will return multiply of max"""
    return b+a*max(x,y)
data1 = myFun2(2,4)
print(data1)
print(myFun2.__annotations__)