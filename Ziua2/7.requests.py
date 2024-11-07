import requests

# print(requests)
# print(requests.__doc__)

response = requests.get('https://pypi.org/')
print(response)
print(response.status_code)
print(response.text)

file_handle  = open('pypi.html', 'w')
file_handle.write(response.text)

file_handle.close()