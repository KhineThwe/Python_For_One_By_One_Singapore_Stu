#returning function from a function
def square(a):
    return a**2

def cube(b):
    return b**3

#fun call
def num(number):
    if number == 1:
        return square#fun return
    else:
        return cube#fun return
if __name__ == '__main__':
    sq = num(1)  # sq ကိုပဲ print ထုတ်ကြည့်မယ်ဆိုရင် memory address တစ်ခု return ပြန်လာတယ်။
    print(sq(3))

    cu = num(2)
    print(cu(4))