import requests
from geolocation import Geolocation

class WeatherClient:
    def __init__(self):
        self.coords=self.get_coords()

    def get_coords(self):
        geolocator = Geolocation("http://ip-api.com/json/?fields=lat,lon")
        return geolocator.get_coords()

    def get_weather(self):
        lat=self.coords['lat']
        lon=self.coords['lon']
        url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
        response = requests.get(url)
        return response.json()['current']

if __name__ == "__main__":
    weather = WeatherClient()
    print(weather.get_weather())