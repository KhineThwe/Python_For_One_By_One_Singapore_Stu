#Variables
#camelCase --> mgMg
#snake_case   ---> mg_mg
#underscore
#eg._mgmg = "student"
#eg.mgmg_ eg. _mg_
#keywords ma ya
#function name ma ya

#assignment operator
val1 = 10
#augmented assignment operator
val1 += 10
#val1 = val1 + 10
#val1 = val1 - 10
val1 -= 10

val1 *= 10
#val1 = val1 * 10

#String
username = 'khine'
password = "7012"
long_string = '''
Wow
Hi
How are you?
'''
print(long_string)

#Type conversion or concatenate
print(type(password))
new_pwd = int(password)#str(pasword)
print(new_pwd,type(new_pwd))

#Escape Sequence
weather = '\t\tIt\'s hot.\nHi'
print(weather)

#formatted strings
name = "khine"
age = 24
print('hi'+name+'.'+'You are'+str(age)+'years old')
print('hi {1} . You are {0} years old'.format(name,age))
print(f'hi {name}.You are {age}')


