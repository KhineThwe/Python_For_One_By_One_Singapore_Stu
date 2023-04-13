#unpacking
#list,tuple ---> can unpack
#set,dictionary ---> cann't unpack

a,b,c = (10,100,1000)
print(a)
print(b)
print(c)
print(type(c))

(k,z,t)=[10,100,1000]
print(k)
print(z)
print(t)
print(type(t))

#string unpacking
(jh,k,l) = 'XYZ'
print(jh,k,l)

dset1 = {'A','B','C','D'}
print(dset1)
for d in dset1:
    print(d)
name,age = ["Khine",24]
print(name,age)
