from fastapi import FastAPI
import get_weather
import schemas

app = FastAPI()

@app.get("/")
def index():
    return {"text": "hello world"}

@app.post("/weather")
def weather(city: schemas.City):
    data = get_weather.get_forecast_data(city)
    return {"weather": data}