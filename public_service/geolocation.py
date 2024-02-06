import requests

class Geolocation:
    def __init__(self,url):
        self.url = url

    def get_coords(self):
        r = requests.get(self.url)
        return r.json()

if __name__ == '__main__':
    g = Geolocation('http://ip-api.com/json/?fields=lat,lon')
    print(g.get_coords())