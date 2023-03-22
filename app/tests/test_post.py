import requests

name = 'Tay'
url = f'http://localhost:5000/callname/{name}'
response = requests.get(url)

print(response.json())
