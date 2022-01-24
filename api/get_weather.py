import requests
from dotenv import load_dotenv
import os
import schemas.weather_api as schemas
load_dotenv()



def get_forecast_data(city: schemas.City):
    BASE_URL = "http://api.openweathermap.org/data/2.5/forecast/"
    API_KEY = os.getenv("WEATHER_API_KEY")
    url = (BASE_URL + f"?id={city.city_id}&lang=ja&units=metric&appid={API_KEY}")
    res = requests.get(url).json()
    forecast_data = {}
    for forecast in res["list"]:
        date = forecast["dt_txt"]
        weather = forecast["weather"][0]["description"]
        temp = forecast["main"]["temp"]
        humidity = forecast["main"]["humidity"] 
        wind = forecast["wind"]["speed"]
        forecast_data[f"{date}"] = {"天気": weather, "気温": temp, "湿度": humidity, "風速": wind} 
        
    return forecast_data

