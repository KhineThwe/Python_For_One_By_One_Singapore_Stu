import json
with open("states.json") as f:
    data = json.load(f)
    print(data)
    print(type(data))

for state in data['states']:
    del state['area_codes']

with open("new_states.json","w") as f1:
    json.dump(data,f1,indent=2)