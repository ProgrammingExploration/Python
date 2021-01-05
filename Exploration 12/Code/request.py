import requests

URL = 'http://127.0.0.1:5000/'

data = requests.post(URL, json={ 'name': 'Om', 'age': 165 })
print(data.json())
