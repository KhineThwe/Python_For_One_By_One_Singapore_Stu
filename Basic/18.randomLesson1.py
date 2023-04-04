#random.choice
import random
#For random.choice#list tuple dictionary --> return random value
name = ['rose','sunflower','lily']
print("Selecting elements: ",random.choice(name))

#For random.sample(population,k) --> population ဆိုတာ example list,set or tuple return list
subject = ['python','java','c','c++','c#','js']
print("Selecting elements: ",random.sample(subject,2))

#random.seed
random.seed(10)
print("Random no from seed(): ",random.random())

#random.shuffle
username = ['rose','sunflower','lily']
print("Before shuffle ",username)
random.shuffle(username)
print("After shuffle ",username)

#random.uniform(start,end)#floating number return floating point number
print("Random no from uniform : ",random.uniform(10.5,20.5))

#random.triangular(low,high,mode) for floating number
print("Triangular: ",random.triangular(10.5,20.5,2.5))


