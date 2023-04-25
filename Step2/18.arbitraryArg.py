#arbitrary argument or end of positional argument
# *
def myFun(*arg):
    print(arg)#return tuple
    for d in arg:
        print(d)
myFun(4,5,6,7,8)

def myFun2(a,b,c,*args):
    print(a)
    print(b)
    print(c)
    print(args)
myFun2(40,50,60,70,80,90)