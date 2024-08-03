import requests

endpoint = "http://127.0.0.1:8000/api/create_product"

response = requests.post(endpoint,json={'title':'Buildings','content':'a'})

print(response.text)