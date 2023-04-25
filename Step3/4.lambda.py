#namesless ---> anonymous function
#no def keyword , no function name
#function obj တစ်ခု return ပြန်ပေးတယ်။
def fun(x,y):
    return y*2+x
#two parameters
x = lambda x,y:y*2+x
print(x)
print(x(3,4))

y = lambda i,j=10:i*j
print(y(2))

#arbitrary
z = lambda x,y,*args:(x,y,args)
print(z(10,20,30,40,50))

