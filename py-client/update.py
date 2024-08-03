import requests

endpoint = "http://127.0.0.1:8000/api/update/1"

response = requests.put(endpoint,json={'title':'Yogeshkannah','content':'Good in coding when comparing to himself'})

print(response.text)