import requests
from dotenv import load_dotenv
import os
load_dotenv()

BASE_URL = "http://api.openweathermap.org/data/2.5/forecast/"
API_KEY = os.getenv("WEATHER_API_KEY")
city_id = "1853295"

def get_forecast_data(city_id):
    url = (BASE_URL + f"?id={city_id}&lang=ja&units=metric&cnt=9&appid={API_KEY}")
    res = requests.get(url).json()
    temp = res["list"][0]["main"]["temp"]
    humidity = res["list"][0]["main"]["humidity"] 
    weather = res["list"][0]["weather"][0]["description"]
    wind = res["list"][0]["wind"]["speed"]
    date = res["list"][0]["dt_txt"]
    print(temp)
    print(humidity)
    print(weather)
    print(wind)
    print(date)

get_forecast_data(city_id)