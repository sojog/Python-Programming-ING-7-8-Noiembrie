import requests
import json
from pprint import pprint
# curl -H "Accept: text/plain" 

response = requests.get("https://icanhazdadjoke.com/", headers={'Accept': 'text/plain'})
print(response.text)

response = requests.get("https://icanhazdadjoke.com/", headers={'Accept': 'application/json'})
print(response.text, type(response.text))

json_dict = json.loads(response.text)
print(json_dict, type(json_dict))
pprint(json_dict)

print("Glumea mea este:", json_dict['joke'])