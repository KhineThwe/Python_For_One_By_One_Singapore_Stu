import json
import requests
# url = " https://api.punkapi.com/v2/beers/1"
# url = " https://api.punkapi.com/v2/beers"
url = " https://api.punkapi.com/v2/beers/random"

r = requests.get(url)
data = json.loads(r.text)
for d in data:
    print("Name: ",d['name'])
    print("Tagline: " ,d['tagline'])
    print("\n")