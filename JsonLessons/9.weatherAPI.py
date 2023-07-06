import json
import requests
#https://openweathermap.org/api
#https://api.openweathermap.org/data/2.5/weather?q=Yangon&appid=81d9fa83140eb4c5be0084535881fc9e
keys = '81d9fa83140eb4c5be0084535881fc9e'
url = 'https://api.openweathermap.org/data/2.5/weather?appid=81d9fa83140eb4c5be0084535881fc9e&q='
cityName = input("Please enter your city name: ")
url += cityName

#method1
# jsonData = requests.get(url).json()
# print(jsonData)

#method2
jsonData = requests.get(url).json()
for i in jsonData:
    print(jsonData[i])
print(jsonData['coord'])

