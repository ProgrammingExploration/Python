import requests

URL = 'http://127.0.0.1:5000'

arr = requests.get(URL + '/all').json()
input()
print(arr)
input()
data = requests.post(URL + '/store', json={ 'name': "PythonAPI" }).json()
input()
print(data)
