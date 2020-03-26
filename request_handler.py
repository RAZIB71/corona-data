import json
from utils import requests_get

class RequestHandler:
    
    def __init__(self):
        self.BASE_URL = "https://corona.lmao.ninja"

    def get_statistics(self):
        url = "{}/{}".format(self.BASE_URL, "all")
        response = requests_get(url)

        return json.loads(response.text)

    def get_countries(self):
        url = "{}/{}".format(self.BASE_URL, "countries")
        response = requests_get(url)

        return json.loads(response.text)

    def get_country(self, country="Bangladesh"):
        url = "{}/{}/{}".format(self.BASE_URL, "countries", country)
        response = requests_get(url)

        return json.loads(response.text)

    def get_countries_historical(self):
        url = "{}/v2/{}".format(self.BASE_URL, "historical")
        response = requests_get(url)

        return json.loads(response.text)

    def get_country_historical(self, country="Bangladesh"):
        url = "{}/v2/{}/{}".format(self.BASE_URL, "historical", country)
        response = requests_get(url)

        return json.loads(response.text)

def test():
    req = RequestHandler()
    
    print(req.get_statistics())
    print(req.get_countries())
    print(req.get_country())
    print(req.get_countries_historical())
    print(req.get_country_historical())

if __name__ == '__main__':
    test()