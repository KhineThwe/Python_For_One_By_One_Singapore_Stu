# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.hexdigits)# 0 --- 9 A B C D E F
# print(string.octdigits)# 0 ---- 7

import secrets
import string
#generate a ten character alphanumeric password
#with at least one lowercase character , at least one uppercase character and at least three digits

alphabet = string.ascii_letters + string.digits#a--->z 0 ---9
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))# 0 to 9
    # for i in range(10):#i=2
    #     password = ''.join(secrets.choice(alphabet))#xY9iippeeppp
    # for c in password:
    #     if(any(c.islower()) and any(c.isupper()) and sum(c.isdigit())>=3):
    #         print(password)
    #         break
    if(any(c.islower() for c in password) and any(c.isupper() for c in password) and
    sum(c.isdigit() for c in password)>=3):
        print(password)
        break
