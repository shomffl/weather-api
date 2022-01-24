import requests
from dotenv import load_dotenv
import os
load_dotenv()

def laundry_exponent(temp:str, humidity:str):
    
    cul = (0.81 * float(temp) + 0.01 * float(humidity) * (0.99 * float(temp) - 14.3) + 46.3)
    return cul

def get_forecast_data(city: str):
    BASE_URL = "http://api.openweathermap.org/data/2.5/forecast/"
    API_KEY = os.getenv("WEATHER_API_KEY")
    url = (BASE_URL + f"?id={city}&lang=ja&units=metric&appid={API_KEY}")
    res = requests.get(url).json()
    forecast_data = {}
    for forecast in res["list"]:
        date = forecast["dt_txt"]
        weather = forecast["weather"][0]["description"]
        temp = forecast["main"]["temp"]
        humidity = forecast["main"]["humidity"] 
        wind = forecast["wind"]["speed"]
        exponent = get_forecast_data(temp, humidity)
        forecast_data[f"{date}"] = {"天気": weather, "気温": temp, "湿度": humidity, "風速": wind, "洗濯指数": exponent} 
        
    return forecast_data



