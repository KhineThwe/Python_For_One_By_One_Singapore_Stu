#Password checker
username = input("What is your name?")
password = input("What is your password?")#yyyyyyyy
password_length = len(password)#3
hidden_password = '*' * password_length

print(f'{username},your password,{hidden_password}')