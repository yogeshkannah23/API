import requests

endpoint = "http://127.0.0.1:8000"

response = requests.get(endpoint,params={'yogesh':['kannah','op']})

print(response.text)
print(response.status_code)
print(response.json()['name'])