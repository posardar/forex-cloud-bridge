from fastapi import FastAPI
import requests

app = FastAPI()

LOCAL_API = "https://lanell-dulotic-catarrhally.ngrok-free.dev/get_data/"


@app.get("/")
def home():
    return {"message": "Cloud Bridge is running 🌍"}


@app.get("/get_data/{timeframe}")
def get_data(timeframe: str):
    try:
        response = requests.get(LOCAL_API + timeframe)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Could not fetch data from local server ({response.status_code})"}
    except Exception as e:

        return {"error": str(e)}
