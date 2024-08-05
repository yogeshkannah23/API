import requests
from getpass import getpass

endpoint = "http://127.0.0.1:8000/auth/"
user_name = 'kalai'
# pass_word = getpass()
pass_word = "yogesh@13"
auth_response = requests.post(endpoint,json={'username':user_name,'password':pass_word})


print(auth_response.json())

if auth_response.status_code == 200:
    endpoint = "http://127.0.0.1:8000/api/update/1"
    token = auth_response.json()['token']
    headers = {
        "Authorization":f"Token {token}"
    }
    response = requests.put(endpoint,headers=headers)

    print(response.text)