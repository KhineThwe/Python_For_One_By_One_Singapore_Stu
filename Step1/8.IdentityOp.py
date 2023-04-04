#Identity op ---> is,is not -----> if they are equal memory address
#if int dat type,string data types ---->
#list [] ----> they are equal but not identical.
a1 =5
a2 = 5
b1= "Hello"
b2 = "Hello"
list1 = [1,2,3]
list2 = [1,2,3]

print("a1 is a2: ",a1 is a2)#same return True else False
print("b1 is b2: ",b1 is b2)


print("a1 is not a2",a1 is not a2)#not same return True else False
print("b1 is not b2",b1 is not b2)

print("list1 is list2",list1 is list2)
print("list1 is not list2",list1 is not list2)