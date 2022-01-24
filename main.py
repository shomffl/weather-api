from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"text": "hello world"}

@app.post("/weather")
def weather():
    return {"text": "hello world"}