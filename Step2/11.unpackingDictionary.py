#1.using unpacking operator ** to unpack dictionary in python
d = {'k1': 10, 'k2': 20, 'a3': 30}

def fun(k1,k2,a3):
    print(k1,k2,a3)
# fun(d['k1'],d['k2'],d['k3'])
fun(**d)

#2
new = {'k0':0,**d}
print(new)
#output --->

#3
#for loop
for k,v in d.items():
    print(k,":",v)

#4
lst = []
for k,v in d.items():
    lst.append((k,v))
print(lst)

#items() function in python3
new_lst = d.items()
print("Using items function: ",*new_lst,type(new_lst))