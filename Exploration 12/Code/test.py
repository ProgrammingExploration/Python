import requests

URL = 'http://localhost:5000'

put = requests.put(URL + '/edit')
print(put)
