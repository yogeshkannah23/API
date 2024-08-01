import requests

endpoint = "http://localhost:8000/"

response = requests.get(endpoint,json={'yogesh':'kannah'})

print(response.text)