import json
person_list = []
with open('json_fake_data.json') as jsonFile:
    data = json.load(jsonFile)
#
# for i in data:
#     print(i,"\n")

    for item in data:
        name = item['name']
        email = item['email']
        balance = item['balance']

        person = {
            'new_name' : name,
            'new_email' : email,
            'new_balance' : balance
        }
        person_list.append(person)

    print(person_list)
