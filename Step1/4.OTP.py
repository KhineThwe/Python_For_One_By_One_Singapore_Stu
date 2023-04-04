import secrets
import string
OTP = '' #initialize
digit = string.digits#0123456789
# randomNo = secrets.choice(digit)
# print(randomNo)
for i in range(6):
    OTP += str(''.join(secrets.choice(digit)))
    #i = 0---> OTP = 3
    #i = 1 ---> OTP = 37
    #i = 2 ---> OTP = 376
    # i = 3---> OTP = 3767
    # i = 4 ---> OTP = 37670
    # i = 5 ---> OTP = 376709
print(f'Your One Time Pad Password: {OTP}')