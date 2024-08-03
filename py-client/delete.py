import requests

delete_id = input("enter the id you want to be deleted.")
try:
    delete_id = int(delete_id)
except:
    raise("The delete id must be numbmer")

if delete_id:
    endpoint = f"http://127.0.0.1:8000/api/delete/{delete_id}"

response = requests.delete(endpoint)

print(response.text)