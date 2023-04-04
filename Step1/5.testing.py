#Operators in Python Programming
#Arithmetic operator
#Relational operator
#Logical operator (and or not)
#membership operator (in,not in)
creditScore1 = 1
creditScore2 = 9
creditScore3 = 13
#and ----> logical operator
# if creditScore1>creditScore2 and creditScore3>creditScore1:
#     print("Both conditions are true!")
# else:
#     print("One condition or both are false")

#or ----> logical operator
# if creditScore1>creditScore2 or creditScore3<creditScore1:
#     print("Both or one conditions are true!")
# else:
#     print("Both are false")

#for not logical operator eg
# isActive = True
# print('not x is',not isActive)

#logical operator eg
# a = False
# if not a:
#     print("Boolean value of a is True")

from random import randint

secret = randint(1, 10)

print("Welcome!")

name = ""
while not name:
    name = input("Enter your name: ").strip()#.strip() removes whitespace at the beginning and at the end
    print(name)
