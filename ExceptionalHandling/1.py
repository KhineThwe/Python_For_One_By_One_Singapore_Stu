#exceptional handling ----> try except finally
""""
try:
   #run ချင်တဲ့code
except:
   #:except ဖြစ်လာတဲ့အချိန်မှာ run မဲ့code
else:
   #:exceptမဖြစ်လာတဲ့အချိန်မှာ run မဲ့code
#try code ---> else block
"""
try:
    file = open("data9.txt", "r")
except Exception as e:
    print("File Cannot Open")
else:
    print("This else statement is running")