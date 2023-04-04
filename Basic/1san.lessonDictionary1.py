user = {
    'name':'Khine',
    'gender':'female'
}
print(user['gender'])
print(user.get('name'))
print(user.get('nationality'))#None
print(user.get('nationality','myanmar'))

password = {"mgmg":123,"koko":345}
print(password.get("mgmg"))
print(password.get("koko"))
print(password.values())