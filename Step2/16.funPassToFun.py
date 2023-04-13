#function passing through a function
#function ထဲမှာ function တစ်ခုကို parameter တစ်ခုအနေနဲ့ ဖြတ်သွားခိုင်းတာ
def square(a):#parameter a#square(3)
    return a**2#3**2=9

def cube(b):#cube(4)
    return b**3#4**3 = 64

def funtofun(funname,n):#funname,parameter 1 ခုရယ်ပါတယ်။
    return funname(n)#return square(3)#cube(4)

if __name__ == '__main__':
    a = funtofun(square,3)#square fun ကို parameter 3 သယ်သွားပြီးတော့သွားခေါ်မယ်
    print('Calling square function: ',a)

    b = funtofun(cube,4)
    print('Calling cube function: ',b)#64