import requests

endpoint = "http://127.0.0.1:8000"

response = requests.post(endpoint,params={'yogesh':['kannah','op']},json={'title':'Guns','content':'Used To shoot someone'})

print(response.text)
