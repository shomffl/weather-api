import requests
from dotenv import load_dotenv
import os
import schemas
import judgement_laundry
load_dotenv()




def get_forecast_data(city: schemas.City):
    BASE_URL = "http://api.openweathermap.org/data/2.5/forecast/"
    API_KEY = os.getenv("WEATHER_API_KEY")
    url = (BASE_URL + f"?id={city.city_id}&lang=ja&units=metric&appid={API_KEY}")
    res = requests.get(url).json()
    forecast_data = {}
    for num, forecast in enumerate(res["list"]):
        date = forecast["dt_txt"]
        weather = forecast["weather"][0]["main"]
        description = forecast["weather"][0]["description"]
        weather_condition = judgement_laundry.weather_condition(weather)
        icon = forecast["weather"][0]["icon"]
        temp = forecast["main"]["temp"]
        humidity = forecast["main"]["humidity"] 
        wind = forecast["wind"]["speed"]
        wind_condtion = judgement_laundry.wind_condition(wind)
        exponent = judgement_laundry.laundry_exponent(temp, humidity)
        recommendation = judgement_laundry.laundry_recommendation(weather, exponent)
        forecast_data[num] = {"日付": date, "天気": {"概要": weather, "詳細": description, "外干しの可否": weather_condition ,"画像": f"http://openweathermap.org/img/wn/{icon}@2x.png"}, "気温": temp, "湿度": humidity, "風":{"風速": wind, "風の状態": wind_condtion},"洗濯指数": exponent, "おすすめ": recommendation} 

    return forecast_data