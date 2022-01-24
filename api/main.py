from fastapi import FastAPI
from . import get_weather

app = FastAPI()

@app.get("/")
def index():
    return {"text": "hello world"}

@app.get("/weather")
def weather():
    city_id = "1853295"
    data = get_weather.get_forecast_data(city_id)
    return {"weather": data}