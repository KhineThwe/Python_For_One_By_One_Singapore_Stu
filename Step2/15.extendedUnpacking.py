#extended unpacking

#1.list unpackingsq = num(1)#sq ကိုပဲ print ထုတ်ကြည့်မယ်ဆိုရင် memory address တစ်ခု return ပြန်လာတယ်။
a,b,*c,d=[1,2,3,4,5,6,7,8,9]#* #list tuple
print(a,b)
print(c)
print(type(c))
print(d)

#tuple unpacking
a,*b = (1,2,3,4,5,6,7,8,9)
print(a)
print(b,type(b))

#string unpacking
a,b,*c = 'python'
print(a,b,c,type(c))

#extended unpacking in righthand-size
l1 = [1,2,3,4,5]
l2= [6,7,8,9]
list = [l1,l2]#nested list
print(list,type(list))
list1  = [*l1,*l2]
print(list1)
print(type(list1))