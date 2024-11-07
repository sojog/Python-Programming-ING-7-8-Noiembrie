import requests
import json

response = requests.get("https://dog.ceo/api/breeds/image/random")
print(response.text)
json_resp = json.loads(response.text)
print(json_resp['message'])

response = requests.get(json_resp['message'])
print(response.content)

with open('image.jpg', 'wb') as file_handle:
    file_handle.write(response.content)

