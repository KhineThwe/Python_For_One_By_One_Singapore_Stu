#Random
#random.random() #return between floating points 0.0 and 1.0
import random
random_no = random.random()
print("Random no : ",random_no)
#int return
#randint(lower,upper) ---> randint(0,9)
#randrange(start,stop,step) ---> randrange(0,10,2)
print("Random no with randint: ",random.randint(0,9))
print("Random no with randrange: ",random.randrange(0,15,3))
