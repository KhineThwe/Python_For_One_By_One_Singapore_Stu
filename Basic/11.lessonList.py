amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
# print(amazon_cart[::-1])
# #although strings are immtable,list is mutable
# amazon_cart[0] = "laptop"
# print(amazon_cart)
# new_cart = amazon_cart[0:3]
# print(new_cart)
# new_cart[1]="baseball"
# print(new_cart)
#
# #List Methods
# #adding
# amazon_cart.append("book")#append doesn't return
# print(amazon_cart)
# #extend another list
# amazon_cart.extend(["tv","headphone"])
# print(amazon_cart)
#
# basketball = [1,2,3,4,5]
# mew_list = basketball.extend([100,101])
# print(mew_list)
#
# #insert
# amazon_cart.insert(4,"aircon")
# print(amazon_cart)
#
# #pop
# a = amazon_cart.pop(4)#pop return removing element
# print(amazon_cart)
# print("After pop",a)
#
# amazon_cart.remove("grapes")#remove doesn't return removing element
# print(amazon_cart)

#sort
amazon_cart.sort()#default ---> ascending order
print(amazon_cart)

# amazon_cart.sort(reverse=True)#descending order
# print(amazon_cart)

#sorting list by length of the values
def myFunc(e):#notebooks = 9 # 'sunglasses' =10#toys-->4#grapes --> 6
    return len(e)

# amazon_cart.sort(key=myFunc) #key = 9#amazon_cart---> [notebooks]#key = 10 ---> ['notebooks,'sunglasses']
# #key=4--> ['toys','notebooks,'sunglasses']
# #key=6 ---> ['toys','grapes','notebooks,'sunglasses']
# print(amazon_cart)

#sorting function
sorted(amazon_cart)
print(amazon_cart)
sorted(amazon_cart,reverse=True)
print(amazon_cart)
sorted(amazon_cart,key=myFunc)
print(amazon_cart)

#copy()
# new_amazon_cart = amazon_cart.copy()
# print(new_amazon_cart)
#
# #reverse()
# amazon_cart.reverse()
# #or
# print(amazon_cart[::-1])