import requests

class APIRequest:
    def __init__(self, url, headers={}):
        self.url = url
        self.headers = headers

    def make_request(self):
        response = requests.get(self.url, headers=self.headers)
        print(response.text)


api_req =  APIRequest("https://icanhazdadjoke.com/", {'Accept': 'application/json'})
api_req.make_request()


api_req2 =  APIRequest("https://api.chucknorris.io/jokes/random", {'Accept': 'application/json'})
api_req2.make_request()