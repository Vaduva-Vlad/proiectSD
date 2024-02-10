import requests
from geolocation import Geolocation

class WeatherClient:
    def __init__(self):
        self.coords=self.get_coords()
        self.weather=self.get_weather()

    def get_coords(self):
        geolocator = Geolocation("http://ip-api.com/json/?fields=lat,lon")
        return geolocator.get_coords()

    def get_weather(self):
        lat=self.coords['lat']
        lon=self.coords['lon']
        url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,rain,showers,snowfall,snow_depth,wind_speed_10m,wind_direction_10m,soil_temperature_0cm,soil_moisture_0_to_1cm"
        response = requests.get(url)
        return response.json()['current']

    def display_results(self):
        print(f"Temperatura: {self.weather['temperature_2m']}")
        print(f"Sansa de ploaie: {self.weather['rain']}")
        print(f"Sansa de ninsoare: {self.weather['snowfall']}")
        if self.weather['snowfall']>0:
            print(f"Adancimea zapezii: {self.weather['snow_depth']}")
        print(f"Viteza vantului: {self.weather['wind_speed_10m']}")
        print(f"Directia vantului: {self.weather['wind_direction_10m']}")
        print(f"Temperatura pamantului: {self.weather['soil_temperature_0cm']}")
        print(f"Umiditatea pamantului: {self.weather['soil_moisture_0_to_1cm']}")

if __name__ == "__main__":
    weather = WeatherClient()
    weather.display_results()