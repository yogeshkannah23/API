import requests

delete_id = input("enter the id you want to be deleted.")

try:
    delete_id = int(delete_id)
except:
    raise("The delete id must be numbmer")

endpoint = "http://127.0.0.1:8000/auth/"
user_name = 'mohan'
# pass_word = getpass()
pass_word = "yogesh@123"
auth_response = requests.post(endpoint,json={'username':user_name,'password':pass_word})

if delete_id and auth_response.status_code == 200:
    endpoint = f"http://127.0.0.1:8000/api/delete/{delete_id}"
    token = auth_response.json()['token']
    headers = {
        "Authorization" : f"Token {token}"
    }
    response = requests.delete(endpoint,headers=headers)

print(response.text)